using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using MeetingOrder.Models;
using MeetingOrder.Authentication;
using Microsoft.EntityFrameworkCore;

namespace MeetingOrder.DataAccess
{
    public class DataAccessProvider : IDataAccessProvider
    {
        private readonly ApplicationDbContext _context;

        public DataAccessProvider(ApplicationDbContext context)
        {
            _context = context;
        }

        public void AddMeetingRecord(Meeting meet)
        {
            _context.meetings.Add(meet);
            _context.SaveChanges();
        }

        public void UpdateMeetingRecord(Meeting meeting)
        {
            _context.meetings.Update(meeting);
            _context.SaveChanges();
        }

        public void DeleteMeetingRecord(string id)
        {
            var entity = _context.meetings.FirstOrDefault(t => t.MeetingId == id);
            _context.meetings.Remove(entity);
            _context.SaveChanges();
        }

        public Meeting GetMeetingSingleRecord(string id)
        {
            return _context.meetings.FirstOrDefault(t => t.MeetingId == id);
        }

        public List<Meeting> GetMeetingRecords()
        {
            return _context.meetings.ToList();
        }
        public IQueryable<Meeting> GetRecords(OwnerParameters ownerParameters)
        {
            IQueryable<Meeting> query = _context.meetings;

            var type = typeof(Meeting);
            var prop = type.GetProperty(ownerParameters.Sort_by);
            if (prop != null)
            {
                var param = Expression.Parameter(type);
                var expr = Expression.Lambda<Func<Meeting, object>>(
                    Expression.Convert(Expression.Property(param, prop), typeof(object)),
                    param
                );
                if (ownerParameters.Sort_type == "desc")
                {
                    query = query.OrderByDescending(expr);
                }
                else
                {
                    query = query.OrderBy(expr);
                }
            }
            var list = (from r in query select r).AsEnumerable();
            if (!string.IsNullOrEmpty(ownerParameters.Search))
            {
                var stringProperties = typeof(Meeting).GetProperties();
                list = list.Where(c => stringProperties.Any(prop => prop.GetValue(c, null).ToString().Contains(ownerParameters.Search)));
            }
            var list1 = list.AsQueryable();
            return list1;
        }
        public bool MeetingExists(string id)
        {
            return _context.meetings.Any(e => e.MeetingId == id);
        }

        public bool InOrder(string id)
        {
            IQueryable<Order> query = _context.orders;
            foreach(var o in query)
            {
                if(o.MeetingId == id)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
