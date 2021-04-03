using MeetingOrder.Authentication;
using MeetingOrder.Models;
using Microsoft.AspNetCore.Identity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace MeetingOrder.Controllers
{
    public class Help
    {
        private readonly ApplicationDbContext _context;

        public Help(ApplicationDbContext context)
        {
            _context = context;
        }
        public bool AlreadySubscribed(string id, IdentityUser user)
        {
            IQueryable<Order> query = _context.orders;
            var list = (from r in query select r).AsEnumerable();
            list = list.Where(c => c.ApplicationUser.Id == user.Id && c.MeetingId == id);
            return list.Count() > 0;
        }
    }
}
