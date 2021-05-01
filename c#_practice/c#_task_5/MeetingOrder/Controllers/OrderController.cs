using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using MeetingOrder.DataAccess;
using MeetingOrder.Models;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using MeetingOrder.Authentication;
using Microsoft.AspNetCore.Identity;
using System.Security.Principal;
using System.Security.Claims;
using Microsoft.Extensions.Caching.Distributed;
using Newtonsoft.Json;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace MeetingOrder.Controllers
{
    /// <summary>
    /// OrderController
    /// </summary>
    [Route("api/Orders")]
    [ApiController]
    public class OrderController : ControllerBase
    {
        private readonly UserManager<ApplicationUser> userManager;
        private readonly IDataAccessProvider _dataAccessProvider;
        private readonly ApplicationDbContext _context;
        private readonly IDistributedCache distributedCache;
        //private readonly Help _helper;
        /// <summary>
        /// OrderController
        /// </summary>
        public OrderController(UserManager<ApplicationUser> userManager, IDataAccessProvider dataAccessProvider, ApplicationDbContext context, IDistributedCache distributedCache)
        {
            this.userManager = userManager;
            this._context = context;
            this._dataAccessProvider = dataAccessProvider;
            this.distributedCache = distributedCache;
           // this._helper = h;
        }
        // GET: api/<OrderController>
        /// <summary>
        /// This GET method returns orders of authorized user
        /// </summary>
        /// <returns>An array of orders</returns>
        [Authorize]
        [HttpGet]
        public IActionResult Get()
        {
            IQueryable<Order> query = _context.orders;
            var list = (from r in query select r).AsEnumerable();
            IdentityUser user = userManager.FindByNameAsync(HttpContext.User.Identity.Name).Result;
            list = list.Where(c => c.ApplicationUserId == user.Id);
            var orders_string = JsonConvert.SerializeObject(query);
            distributedCache.SetString("orders", orders_string);
            return Ok(list);
        }
        /// <summary>
        /// This GET method returns particular order of authorized user
        /// </summary>
        /// <returns>Order</returns>
        /// <response code="400">If order with id doesn't exist or body is invalid</response>
        // GET api/<OrderController>/5
        [Authorize]
        [HttpGet("{id}")]
        public IActionResult Get(string id)
        {
            IdentityUser user = userManager.FindByNameAsync(HttpContext.User.Identity.Name).Result;
            if (_context.orders.Any(t => t.OrderId == id)) {
                Order order = _context.orders.FirstOrDefault(t => t.OrderId == id);
                if (order.ApplicationUser.UserName == user.UserName)
                {
                    return Ok(_context.orders.FirstOrDefault(t => t.OrderId == id));
                }
                else
                {
                    return Unauthorized();
                }
            }
            else
            {
                return BadRequest(new Responce { Message = "Not found" });
            }
        }
        /// <summary>
        /// This POST method subscribes authorized user on chosen meeting
        /// </summary>
        /// <returns>An array of meetings</returns>
        /// <response code="400">If meeting with id doesn't exist or body is invalid</response>
        // POST api/<OrderController>
        [Authorize]
        [HttpPost]
        public IActionResult Post([FromBody] OrderForm model)
        {
            IdentityUser user = userManager.FindByNameAsync(HttpContext.User.Identity.Name).Result;
            if (ModelState.IsValid)
            {
                IQueryable<Order> query = _context.orders;
                var list = (from r in query select r).AsEnumerable();
                list = list.Where(c => c.ApplicationUserId == user.Id && c.MeetingId == model.MeetingId);
                if (list.Count() > 0)
                {
                    return BadRequest(new Responce { Message="You have already subscribed on it" });
                }
                Order o = new Order();
                if (_dataAccessProvider.MeetingExists(model.MeetingId) == false)
                {
                    return BadRequest(new Responce { Message = "No such meeting" });
                }
                Meeting meet = _context.meetings.FirstOrDefault(t => t.MeetingId == model.MeetingId);
                if (meet.Count == 0)
                {
                    return BadRequest(new Responce { Message = "No available places" });
                }
                meet.Count -= 1;
                o.Meeting = meet;
                Guid obj = Guid.NewGuid();
                o.OrderId = obj.ToString();
                o.ApplicationUser = (ApplicationUser)user;
                _context.orders.Add(o);
                _context.SaveChanges();
                IQueryable<Order> query1 = _context.orders;
                var orders_string = JsonConvert.SerializeObject(query1.ToList());
                distributedCache.SetString("orders", orders_string);
                return Ok(o);
            }
            return BadRequest(new Responce { Message = "Order form is not valid" });
        }
    }
}
