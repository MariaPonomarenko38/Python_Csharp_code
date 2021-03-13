using System;
using System.Collections.Generic;
using System.Text;
using WebApplication1.Controllers;
using WebApplication1.Models;
using WebApplication1.DataAccess;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using System.Linq.Expressions;

namespace XUnitTestProject1
{
    class MeetingFake : IDataAccessProvider
    {
        private readonly List<Meeting> _meets;

        public MeetingFake()
        {
            _meets = new List<Meeting>()
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
        }
        public void AddMeetingRecord(Meeting meet)
        {
            meet.Id = new Guid().ToString();
            _meets.Add(meet);
        }

        public void DeleteMeetingRecord(string id)
        {
            var entity = _meets.FirstOrDefault(t => t.Id == id);
            _meets.Remove(entity);
        }

        public Meeting GetMeetingSingleRecord(string id)
        {
            return _meets.FirstOrDefault(t => t.Id == id);
        }

        public IEnumerable<Meeting> GetRecords(OwnerParameters ownerParameters)
        {
            IQueryable<Meeting> query = _meets.AsQueryable();

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
            var list1 = list.AsEnumerable();
            return list1.ToList();
        }

        public bool MeetingExists(string id)
        {
            return _meets.Any(t => t.Id == id);
        }

        public void UpdateMeetingRecord(Meeting meet)
        {
            for (int i = 0; i < _meets.Count(); i++)
            {
                if (_meets[i].Id == meet.Id)
                {
                    _meets[i] = meet;
                }
            }
        }
    }
}
