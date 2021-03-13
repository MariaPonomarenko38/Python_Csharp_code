using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using WebApplication1.Models;

namespace WebApplication1.DataAccess
{
    public interface IDataAccessProvider
    {
        void AddMeetingRecord(Meeting meet);
        void UpdateMeetingRecord(Meeting meet);
        void DeleteMeetingRecord(string id);
        Meeting GetMeetingSingleRecord(string id);
        IEnumerable<Meeting> GetRecords(OwnerParameters ownerParameters);
        bool MeetingExists(string id);
    }
}
