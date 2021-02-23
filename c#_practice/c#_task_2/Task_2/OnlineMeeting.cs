using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;
using System.Threading.Tasks;
using System.ComponentModel;

namespace Task_2
{
    public class Default
    {
        public static string m = DateTime.Now.AddDays(5).ToString("dd.MM.yyyy");
        public static string[] values = { "1", m, "13:13", "19:15", "http://somelink.com", "J J", "K K" };
    }
    public class OnlineMeeting
    {
        int id;
        DateTime date;
        DateTime start_time;
        DateTime end_time;
        string meeting_url;
        string owner;
        string participant;

        public int ID
        {
            get { return id; }
            set { id = value; }
        }
        public DateTime Date
        {
            get { return date; }
            set { date = value; }
        }
        public DateTime Start_time
        {
            get { return start_time; }
            set { start_time = value; }
        }
        public DateTime End_time
        {
            get { return end_time; }
            set { end_time = Validate.TimeConflict(start_time, value); }
        }
        public string URL
        {
            get { return meeting_url; }
            set { meeting_url = Validate.CheckUrl(value); }
        }
        public string Owner
        {
            get { return owner;}
            set { owner = Validate.CheckPerson(value); }
        }
        public string Participant
        {
            get { return participant;}
            set { participant = Validate.CheckPerson(value); }
        }

        public OnlineMeeting()
        {
            int i = 0;
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var prop in props)
            {
                prop.SetValue(this, Convert.ChangeType(Default.values[i], prop.PropertyType));
                i++;
            }
        }
        public OnlineMeeting(string s)
        {
            string[] l = s.Split(';');
            if(l.Length != 7)
            {
                List<string> m = l.ToList();
                m.AddRange(Enumerable.Repeat("", 7 - l.Length));
            }
            int i = 0;
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var prop in props)
            {
                prop.SetValue(this, Convert.ChangeType(l[i], prop.PropertyType));
                i++;
            }
        }
        public string Get(string s)
        {
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var item in props)
            {
                if (item.Name == s)
                {
                    return Convert.ToString(item.GetValue(this));
                }
            }
            return "No such field";
        }
        public bool search(string s)
        {
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var item in props)
            {
                string m = Convert.ToString(item.GetValue(this));
                if (m.Contains(s))
                {
                    return true;
                }
            }
            return false;
        }
        public override String ToString()
        {
            string res = "";
            PropertyInfo[] props = this.GetType().GetProperties();
            foreach (var prop in props)
            {
                if (prop.Name == "Start_time" || prop.Name == "End_time")
                {
                    DateTime dt = DateTime.Parse(prop.GetValue(this).ToString());
                    res += Convert.ToString(dt.TimeOfDay) + ";";
                    continue;
                }
                res += prop.GetValue(this).ToString() + ";";
            }
            res = res.Substring(0, res.Length - 1);
            return res;
        }
    }
}
