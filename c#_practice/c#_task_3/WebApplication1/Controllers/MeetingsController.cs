using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using WebApplication1.DataAccess;
using WebApplication1.Models;

namespace WebApplication2.Controllers
{
    [Route("api/Meetings")]
    public class MeetingsController : ControllerBase
    {
        private readonly IDataAccessProvider _dataAccessProvider;

        public MeetingsController(IDataAccessProvider dataAccessProvider)
        {
            _dataAccessProvider = dataAccessProvider;
        }

        [HttpGet]
        public IEnumerable<Meeting> GetMeetings([FromQuery] OwnerParameters ownerParameters)
        {
            return _dataAccessProvider.GetRecords(ownerParameters);
        }

        [HttpPost]
        public IActionResult Create([FromBody] Meeting meet)
        {
            if (ModelState.IsValid)
            {
                Guid obj = Guid.NewGuid();
                meet.Id = obj.ToString();
                _dataAccessProvider.AddMeetingRecord(meet);
                return Ok("Meeting was successfully added");
            }
            return BadRequest(ModelState);
        }

        [HttpGet("{id}")]
        public ActionResult<Meeting> Details(string id)
        {
            if (_dataAccessProvider.MeetingExists(id) == false)
            {
                return NotFound("Meeting doesn't exist");
            }
            return _dataAccessProvider.GetMeetingSingleRecord(id);
        }

        [HttpPut]
        public IActionResult Edit([FromBody] Meeting meet)
        {
            if (_dataAccessProvider.MeetingExists(meet.Id) == false)
            {
                return BadRequest("Meeting with this id doesn't exist");
            }
            if (ModelState.IsValid)
            {
                _dataAccessProvider.UpdateMeetingRecord(meet);
                return Ok("Meeting was updated");
            }
            return BadRequest(ModelState);
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteConfirmed(string id)
        {
            var data = _dataAccessProvider.GetMeetingSingleRecord(id);
            if (data == null)
            {
                return NotFound("No meeting with such id");
            }
            _dataAccessProvider.DeleteMeetingRecord(id);
            return Ok("Meeting was deleted");
        }
    }
}
