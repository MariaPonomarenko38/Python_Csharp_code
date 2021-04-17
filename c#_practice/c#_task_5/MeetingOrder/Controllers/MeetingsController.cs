using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using MeetingOrder.DataAccess;
using MeetingOrder.Models;
using MeetingOrder.Authentication;
using LightQuery;
using Microsoft.AspNetCore.Authorization;
using System.Linq;
using Microsoft.Extensions.Caching.Distributed;
using Newtonsoft.Json;

namespace MeetingOrder.Controllers
{
    /// <summary>
    /// Meetings Controller responsible for GET/POST/PUT/DELETE for managing meetings
    /// </summary>
    [Route("api/Meetings")]
    public class MeetingsController : ControllerBase
    {
        private readonly IDataAccessProvider _dataAccessProvider;
        private readonly IDistributedCache distributedCache;
        /// <summary>
        /// Meetings Controller
        /// </summary>
        public MeetingsController(IDataAccessProvider dataAccessProvider, IDistributedCache distributedCache)
        {
            _dataAccessProvider = dataAccessProvider;
            this.distributedCache = distributedCache;
        }
        /// <summary>
        /// This GET method returns meetings filtered by ownerParameters
        /// </summary>
        /// <param name="ownerParameters"></param>
        /// <returns>An array of meetings</returns>
        [Authorize]
        [LightQuery(forcePagination: false, defaultPageSize: 3)]
        [ProducesResponseType(typeof(IEnumerable<Meeting>), 200)]
        [HttpGet]
        public IActionResult GetMeetings([FromQuery] OwnerParameters ownerParameters)
        {
            //IQueryable values = _dataAccessProvider.GetRecords(ownerParameters).AsQueryable();
            var meetings = new List<Meeting>();
            if(string.IsNullOrEmpty(distributedCache.GetString("meetings")))
            {
                meetings = _dataAccessProvider.GetRecords(ownerParameters).ToList();
                var meetings_string = JsonConvert.SerializeObject(meetings);
                distributedCache.SetString("meetings", meetings_string);
            }
            else
            {
                meetings = _dataAccessProvider.GetRecords(ownerParameters).ToList();
                var meetings_string = JsonConvert.SerializeObject(meetings);
                distributedCache.SetString("meetings", meetings_string);
                var meetingFromCache = distributedCache.GetString("meetings");
                meetings = JsonConvert.DeserializeObject<List<Meeting>>(meetingFromCache);
            }
            //return Ok(values);
            return Ok(meetings.AsQueryable());
        }
        //[Authorize(Roles = UserRoles.Admin)]
        /// <summary>
        /// This POST method adds new meeting item to database
        /// </summary>
        /// <param name="meet"></param>
        /// <response code="400">If item is invalid</response>
        [MyAuthorize(RoleEnum=UserRoles.Admin)]
        [HttpPost]
        public IActionResult Create([FromBody] Meeting meet)
        {
            if (ModelState.IsValid)
            {
                Guid obj = Guid.NewGuid();
                meet.MeetingId = obj.ToString();
                _dataAccessProvider.AddMeetingRecord(meet);
                var meetings = _dataAccessProvider.GetRecords(new OwnerParameters()).ToList();
                var meetings_string = JsonConvert.SerializeObject(meetings);
                distributedCache.SetString("meetings", meetings_string);
                return Ok(new MeetingResponce { obj = meet, message = "Created" });
            }
            return BadRequest(ModelState);
        }
        /// <summary>
        /// This GET method returns meeting with particular id
        /// </summary>
        /// <param name="id"></param>
        /// <returns>Meeting object</returns>
        /// <response code="400">If meeting doesn't exist</response>
        [Authorize]
        [HttpGet("{id}")]
        public ActionResult<Meeting> Details(string id)
        {
            if (_dataAccessProvider.MeetingExists(id) == false)
            {
                return NotFound(new MeetingResponce {message = "Meeting doesn't exist" });
            }
            return _dataAccessProvider.GetMeetingSingleRecord(id);
        }
        /// <summary>
        /// This PUT method changes meeting values 
        /// </summary>
        /// <param name="meet"></param>
        /// <response code="400">If meeting with id doesn't exist or body is invalid</response>
        //[Authorize(Roles = UserRoles.Admin)]
        [MyAuthorize(RoleEnum = UserRoles.Admin)]
        [HttpPut]
        public IActionResult Edit([FromBody] Meeting meet)
        {
            if (_dataAccessProvider.MeetingExists(meet.MeetingId) == false)
            {
                return BadRequest(new MeetingResponce { message = "Meeting with this id doesn't exist" });
            }
            if (ModelState.IsValid)
            {
                _dataAccessProvider.UpdateMeetingRecord(meet);
                var meetings = _dataAccessProvider.GetRecords(new OwnerParameters()).ToList();
                var meetings_string = JsonConvert.SerializeObject(meetings);
                distributedCache.SetString("meetings", meetings_string);
                return Ok(new MeetingResponce { obj = meet, message = "Created" });
            }
            return BadRequest(ModelState);
        }
        /// <summary>
        /// This DELETE method removes meeting with particular id from database
        /// </summary>
        /// <param name="id"></param>
        /// <response code="400">If meeting with id doesn't exist</response>
        //[Authorize(Roles = UserRoles.Admin)]
        [MyAuthorize(RoleEnum = UserRoles.Admin)]
        [HttpDelete("{id}")]
        public IActionResult DeleteConfirmed(string id)
        {
            var data = _dataAccessProvider.GetMeetingSingleRecord(id);
            if (data == null)
            {
                return NotFound(new MeetingResponce { message = "No meeting with such id" });
            }
            _dataAccessProvider.DeleteMeetingRecord(id);
            var meetings = _dataAccessProvider.GetRecords(new OwnerParameters()).ToList();
            var meetings_string = JsonConvert.SerializeObject(meetings);
            distributedCache.SetString("meetings", meetings_string);
            return Ok(new MeetingResponce { message = "Deleted" });
        }
    }
}
