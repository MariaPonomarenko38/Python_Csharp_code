using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using WebApplication1.Models;

namespace WebApplication1.DataAccess
{
    public interface IDataAccessProvider
    {
        Meeting AddMeetingRecord(Meeting meet);
        void UpdateMeetingRecord(Meeting meet);
        string DeleteMeetingRecord(string id);
        Meeting GetMeetingSingleRecord(string id);
        IEnumerable<Meeting> GetRecords(OwnerParameters ownerParameters);
        bool MeetingExists(string id);
    }
}
