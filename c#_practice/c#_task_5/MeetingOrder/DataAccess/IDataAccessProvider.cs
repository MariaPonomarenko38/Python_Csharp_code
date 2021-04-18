using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MeetingOrder.Models;

namespace MeetingOrder.DataAccess
{
    public interface IDataAccessProvider
    {
        void AddMeetingRecord(Meeting meet);
        void UpdateMeetingRecord(Meeting meet);
        void DeleteMeetingRecord(string id);
        Meeting GetMeetingSingleRecord(string id);
        List<Meeting> GetMeetingRecords();
        IQueryable<Meeting> GetRecords(OwnerParameters ownerParameters);
        bool MeetingExists(string id);
        bool InOrder(string id);
    }
}
