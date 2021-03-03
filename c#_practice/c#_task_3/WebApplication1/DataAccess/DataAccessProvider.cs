using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using WebApplication1.Models;
using Microsoft.EntityFrameworkCore;

namespace WebApplication1.DataAccess
{
    public class DataAccessProvider : IDataAccessProvider
    {
        private readonly MeetingContext _context;

        public DataAccessProvider(MeetingContext context)
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
            var entity = _context.meetings.FirstOrDefault(t => t.Id == id);
            _context.meetings.Remove(entity);
            _context.SaveChanges();
        }

        public Meeting GetMeetingSingleRecord(string id)
        {
            return _context.meetings.FirstOrDefault(t => t.Id == id);
        }

        public List<Meeting> GetMeetingRecords()
        {
            return _context.meetings.ToList();
        }
        public IEnumerable<Meeting> GetRecords(OwnerParameters ownerParameters)
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
            if (!string.IsNullOrEmpty(ownerParameters.Search))
            {
                query = query.Where(
                    c => c.Owner.Contains(ownerParameters.Search) || c.Date.ToString().Contains(ownerParameters.Search) ||
                         c.Start_time.Contains(ownerParameters.Search) || c.End_time.Contains(ownerParameters.Search) ||
                         c.Url.Contains(ownerParameters.Search) || c.Participant.Contains(ownerParameters.Search));
            }
            return query.Skip((ownerParameters.PageNumber - 1) * ownerParameters.PageSize).Take(ownerParameters.PageSize);
        }
        public bool MeetingExists(string id)
        {
            return _context.meetings.Any(e => e.Id == id);
        }
    }
}
