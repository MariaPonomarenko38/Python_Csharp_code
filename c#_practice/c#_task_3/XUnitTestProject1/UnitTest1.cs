using System;
using System.Collections.Generic;
using System.Text;
using WebApplication1.Models;
using WebApplication1.DataAccess;
using WebApplication1.Controllers;
using Xunit;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Linq;
using Moq;

namespace XUnitTestProject1
{
    public class UnitTest1
    {
        private OwnerParameters o = new OwnerParameters();

        [Fact]
        public void Get()
        {
            var mock = new Mock<IDataAccessProvider>();
            mock.Setup(repo => repo.GetRecords(o)).Returns(meets);
            var controller = new MeetingsController(mock.Object);
            var Result = controller.GetMeetings(o);

            var OkResult = Assert.IsType<OkObjectResult>(Result.Result);
            var resultObj = (List<Meeting>)OkResult.Value;
            Assert.Equal(2, resultObj.ToList().Count());
        }
        [Fact]
        public void Get_id_Ok()
        {
            var mock = new Mock<IDataAccessProvider>();

            string id = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200";
            
            mock.Setup(repo => repo.GetMeetingSingleRecord(id)).Returns(meet);
            var controller = new MeetingsController(mock.Object);
            var Result = controller.Details(id);

            var OkResult = Assert.IsType<OkObjectResult>(Result.Result);
            var resultObj = (Responce)OkResult.Value;
            Assert.Equal("13:40", resultObj.meeting.Start_time);
        }
        [Fact]
        public void Get_id_NotFound()
        {
            var mock = new Mock<IDataAccessProvider>();

            string id = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200";

            mock.Setup(repo => repo.GetMeetingSingleRecord(id)).Returns((Meeting)null);
            var controller = new MeetingsController(mock.Object);
            var Result = controller.Details(id);

            var OkResult = Assert.IsType<NotFoundObjectResult>(Result.Result);
        }
        [Fact]
        public void Delete_Ok()
        {
            const string DeletedId = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200";
            
            var mock = new Mock<IDataAccessProvider>();
            mock.Setup(repo => repo.GetMeetingSingleRecord(DeletedId)).Returns(meet);
            mock.Setup(repo => repo.DeleteMeetingRecord(DeletedId)).Returns(DeletedId);
            var controller = new MeetingsController(mock.Object);
            var Result = controller.DeleteConfirmed(DeletedId);

            var OkResult = Assert.IsType<OkObjectResult>(Result.Result);
        }
        [Fact]
        public void Delete_NotFound()
        {
            const string DeletedId = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200";

            var mock = new Mock<IDataAccessProvider>();

            mock.Setup(repo => repo.GetMeetingSingleRecord(DeletedId)).Returns((Meeting)null);
            mock.Setup(repo => repo.DeleteMeetingRecord(DeletedId)).Returns(DeletedId);
            var controller = new MeetingsController(mock.Object);
            var Result = controller.DeleteConfirmed(DeletedId);

            var OkResult = Assert.IsType<NotFoundObjectResult>(Result.Result);
        }
        [Fact]
        public void Add_Valid()
        {
            var mock = new Mock<IDataAccessProvider>();
            string id = new Guid().ToString();
           
            var controller = new MeetingsController(mock.Object);
            var Result1 = controller.Create(meet);
            mock.Verify(r => r.AddMeetingRecord(meet));
        }
        [Fact]
        public void Edit_Ok()
        {
            var mock = new Mock<IDataAccessProvider>();

            var controller = new MeetingsController(mock.Object);

            mock.Setup(r => r.MeetingExists("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200")).Returns(true);
            var Result = controller.Edit(meet);
            mock.Verify(svc => svc.UpdateMeetingRecord(It.IsAny<Meeting>()),
                  Times.Once());
            var OkResult = Assert.IsType<OkObjectResult>(Result.Result);
            var resultObj = (Responce)OkResult.Value;
            Assert.Equal("20:40", resultObj.meeting.End_time);
        }
        [Fact]
        public void Edit_NotFound()
        {
            var mock = new Mock<IDataAccessProvider>();

            var controller = new MeetingsController(mock.Object);

            mock.Setup(r => r.MeetingExists("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200")).Returns(null);
            Meeting m = new Meeting();
            var Result = controller.Edit(m);

            var OkResult = Assert.IsType<BadRequestObjectResult>(Result.Result);
        }
        [Fact]
        public void Add_Invalid()
        {
            var mock = new Mock<IDataAccessProvider>();

            Meeting m = new Meeting();

            var controller = new MeetingsController(mock.Object);
            controller.ModelState.AddModelError("Owner", "Required");
            var Result = controller.Create(m);

            var redirectToActionResult = Assert.IsType<BadRequestObjectResult>(Result);

        }

        List<Meeting> meets = new List<Meeting>()
        {
            new Meeting {Id = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200",
            Date = DateTime.Parse("2021-02-03"),
            Start_time = "13:40",
            End_time = "14:40",
            Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
            Owner = "Maria Ponomarenko",
            Participant = "David Brown"},

            new Meeting {Id = "815accac-fd5b-478a-a9d6-f171a2f6ae7f",
            Date = DateTime.Parse("2021-06-09"),
            Start_time = "12:40",
            End_time = "19:40",
            Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
            Owner = "Molly Cooper",
            Participant = "James Lie"},
        };
        Meeting meet = new Meeting()
        {
            Id = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200",
            Date = DateTime.Parse("2021-02-03"),
            Start_time = "13:40",
            End_time = "20:40",
            Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
            Owner = "Maria Ponomarenko",
            Participant = "David Brown"
        };
    }
}
