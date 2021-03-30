using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using WebApplication1.DataAccess;
using WebApplication1.Models;
using LightQuery;
using System.ComponentModel.DataAnnotations;
using Newtonsoft.Json;

namespace WebApplication1.Controllers
{
    /// <summary>
    /// Meetings Controller responsible for GET/POST/PUT/DELETE for managing meetings
    /// </summary>
    [Route("api/Meetings")]
    public class MeetingsController : ControllerBase
    {
        private readonly IDataAccessProvider _dataAccessProvider;

        public MeetingsController(IDataAccessProvider dataAccessProvider)
        {
            _dataAccessProvider = dataAccessProvider;
        }
        /// <summary>
        /// This GET method returns meetings filtered by ownerParameters
        /// </summary>
        /// <param name="ownerParameters"></param>
        /// <returns>An array of meetings</returns>
        [LightQuery(forcePagination: false, defaultPageSize: 3)]
        [ProducesResponseType(typeof(IEnumerable<Meeting>), 200)]
        [HttpGet]
        public ActionResult<IEnumerable<Meeting>> GetMeetings([FromQuery] OwnerParameters ownerParameters)
        {
            var values = _dataAccessProvider.GetRecords(ownerParameters);
            return Ok(values);
        }
        /// <summary>
        /// This POST method adds new meeting item to database
        /// </summary>
        /// <param name="meet"></param>
        /// <response code="400">If item is invalid</response>
        [HttpPost]
        public IActionResult Create([FromBody] Meeting meet)
        {
            if (ModelState.IsValid)
            {
                Guid obj = Guid.NewGuid();
                meet.Id = obj.ToString();
                Meeting added_meet = _dataAccessProvider.AddMeetingRecord(meet);
                return Ok(new Responce { meeting = added_meet, message = "Meeting was successfully added" });
            }
            return BadRequest(ModelState);
        }
        /// <summary>
        /// This GET method returns meeting with particular id
        /// </summary>
        /// <param name="id"></param>
        /// <returns>Meeting object</returns>
        /// <response code="400">If meeting doesn't exist</response>
        [HttpGet("{id}")]
        public ActionResult<Meeting> Details(string id)
        {
            var item = _dataAccessProvider.GetMeetingSingleRecord(id);
            if (item == null)
            {
                return NotFound(new Responce { message = "Not found" });
            }
            return Ok(new Responce { meeting = item, message = "Meeting was found" });
        }
        /// <summary>
        /// This PUT method changes meeting values 
        /// </summary>
        /// <param name="meet"></param>
        /// <response code="400">If meeting with id doesn't exist or body is invalid</response>
        [HttpPut]
        public ActionResult<Meeting> Edit([FromBody] Meeting meet)
        {
            if (_dataAccessProvider.MeetingExists(meet.Id) == false)
            {
                return BadRequest("Meeting with this id doesn't exist");
            }
            if (ModelState.IsValid)
            {
                _dataAccessProvider.UpdateMeetingRecord(meet);
                return Ok(new Responce { meeting = meet, message = "Meeting was updated" });
            }
            return BadRequest(ModelState);
        }
        /// <summary>
        /// This DELETE method removes meeting with particular id from database
        /// </summary>
        /// <param name="id"></param>
        /// <response code="400">If meeting with id doesn't exist</response>
        [HttpDelete("{id}")]
        public ActionResult<string> DeleteConfirmed(string id)
        {
            var data = _dataAccessProvider.GetMeetingSingleRecord(id);
            if (data == null)
            {
                return NotFound("No meeting with such id");
            }
            var b = _dataAccessProvider.DeleteMeetingRecord(id);
            return Ok(new Responce { message = $"Meeting {b} was deleted" });
        }
    }
}
