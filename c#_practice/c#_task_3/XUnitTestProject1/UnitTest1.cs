using Microsoft.AspNetCore.Mvc.Testing;
using System;
using System.Net.Http;
using Xunit;
using WebApplication1.Models;
using System.Threading.Tasks;
using WebApplication1.Controllers;
using WebApplication1.DataAccess;
using Microsoft.AspNetCore.Mvc;
using XUnitTestProject1;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Linq;

namespace XUnitTestProject1
{
    public class UnitTest1
    {
        MeetingsController _controller;
        IDataAccessProvider _service;
        public UnitTest1()
        {
            _service = new MeetingFake();
            _controller = new MeetingsController(_service);
        }

        [Fact]
        public void Get_ReturnsOkResult()
        {
            OwnerParameters o = new OwnerParameters();
            var okResult = _controller.GetMeetings(o);
            Assert.IsType<OkObjectResult>(okResult.Result);
        }
        [Fact]
        public void GetById_ReturnsOkResult()
        {
            var testGuid = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200";
            var okResult = _controller.Details(testGuid);
            Assert.IsType<OkObjectResult>(okResult.Result);
        }
        [Fact]
        public void Get_ReturnsAllItems()
        {
            OwnerParameters o = new OwnerParameters();
            var okResult = _controller.GetMeetings(o).Result as OkObjectResult;
            var items = Assert.IsType<List<Meeting>>(okResult.Value);
            Assert.Equal(2, items.Count());
        }
        [Fact]
        public void Change_ReturnOk()
        {
            Meeting m = new Meeting
            {
                Id = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200").ToString(),
                Date = DateTime.Parse("2021-02-03"),
                Start_time = "13:40",
                End_time = "15:40",
                Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
                Owner = "Mkfjgk Fgklfg",
                Participant = "riuroi krjtlrt"
            };
            var respo = _controller.Edit(m);
            var t = _service.GetMeetingSingleRecord("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200");
            Assert.IsType<OkObjectResult>(respo);
            Assert.Equal("15:40", t.End_time);
        }

        [Fact]
        public void Remove_ExistingGuidPassed_ReturnsOkResult()
        {
            var existingGuid = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200").ToString();
            var okResponse = _controller.DeleteConfirmed(existingGuid);
            Assert.IsType<OkObjectResult>(okResponse);
        }
        [Fact]
        public void Remove_NotExistingGuidPassed_ReturnsNotFoundResponse()
        {
            var notExistingGuid = Guid.NewGuid().ToString();
            var badResponse = _controller.DeleteConfirmed(notExistingGuid);
            Assert.IsType<NotFoundObjectResult>(badResponse);
        }
        [Fact]
        public void Remove_ExistingGuidPassed_RemovesOneItem()
        {
            OwnerParameters o = new OwnerParameters();
            var existingGuid = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200").ToString();
            var okResponse = _controller.DeleteConfirmed(existingGuid);
            Assert.Equal(1, _service.GetRecords(o).Count());
        }
        [Fact]
        public void Get_Search()
        {
            OwnerParameters o = new OwnerParameters();
            o.Search = "James";
            var okResult = _controller.GetMeetings(o).Result as OkObjectResult;
            var items = Assert.IsType<List<Meeting>>(okResult.Value);
            Assert.Equal(1, items.Count());
        }
        [Fact]
        public void Get_Sort()
        {
            OwnerParameters o = new OwnerParameters();
            o.Sort_by = "Start_time";
            var okResult = _controller.GetMeetings(o).Result as OkObjectResult;
            var items = Assert.IsType<List<Meeting>>(okResult.Value);
            for (int i = 0; i < items.Count(); i++)
            {
                Assert.True(EqualsMeet(SortedList()[i], items[i]));
                break;
            }
        }
        [Fact]
        public void Add_Valid()
        {
            Meeting testItem = new Meeting()
            {
                Date = DateTime.Parse("2021-06-09"),
                Start_time = "12:40",
                End_time = "19:40",
                Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
                Owner = "Molly Cooper",
                Participant = "James Lie"
            };
            var createdResponse = _controller.Create(testItem);
            Assert.IsType<OkObjectResult>(createdResponse);
        }
        [Fact]
        public void Add_NotValid()
        {
            var testItem = new Meeting()
            {
                Date = DateTime.Parse("2021-06-09"),
                End_time = "19:40",
                Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
                Owner = "Molly Cooper",
                Participant = "James Lie"
            };
            _controller.ModelState.AddModelError("Start_time", "Required");
            var createdResponse = _controller.Create(testItem);
            Assert.IsType<BadRequestObjectResult>(createdResponse);
        }
        private List<Meeting> SortedList()
        {
            var meets1 = new List<Meeting>
            {
                new Meeting {Id = "815accac-fd5b-478a-a9d6-f171a2f6ae7f",
                Date = DateTime.Parse("2021-06-09"),
                Start_time = "12:40",
                End_time = "19:40",
                Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
                Owner = "Molly Cooper",
                Participant = "James Lie"},

                new Meeting {Id = "ab2bd817-98cd-4cf3-a80a-53ea0cd9c200",
                Date = DateTime.Parse("2021-02-03"),
                Start_time = "13:40",
                End_time = "14:40",
                Url = "https://blog.reedsoy.com/writing-apps/#11__hemingway",
                Owner = "Maria Ponomarenko",
                Participant = "David Brown"},

            };
            return meets1;
        }
        private bool EqualsMeet(Meeting meet, Meeting meet1)
        {
            var stringProperties = typeof(Meeting).GetProperties();
            foreach (var a in stringProperties)
            {
                if (a.Name == "Date")
                {
                    if (a.GetValue(meet).ToString() != a.GetValue(meet1).ToString())
                    {
                        return false;
                    }
                }
                else if (a.GetValue(meet) != a.GetValue(meet1))
                {
                    return false;
                }
            }
            return true;
        }
    }
}
