using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;
using System.Threading.Tasks;

namespace Task_1
{
    public class OnlineMeeting
    {
        string id;
        string date;
        string start_time;
        string end_time;
        string meeting_url;
        string owner;
        string participant;

        public OnlineMeeting(string s)
        {
            String[] l = s.Split(';');
            id = l[0];
            date = l[1];
            start_time = l[2];
            end_time = l[3];
            meeting_url = l[4];
            owner = l[5];
            participant = l[6];
        }
        public List<object> GetFields()
        {
            var bindingFlags = BindingFlags.Instance | BindingFlags.NonPublic;
            List<object> listValues = this.GetType().GetFields(bindingFlags).Select(field => field.GetValue(this)).ToList();
            return listValues;
        }
        public string Get(string s)
        {
            string[] fields = { "id", "date", "start_time", "end_time", "meeting_url", "owner", "participant" };
            int i = 0;
            foreach (var item in GetFields())
            {
                if (fields[i] == s)
                {
                    return Convert.ToString(item);
                }
                i++;
            }
            return "No such field";
        }
        public void Set(string s, string val)
        {
            Type obj = typeof(OnlineMeeting);
            var bindingFlags = BindingFlags.Instance | BindingFlags.NonPublic;
            obj.GetField(s, bindingFlags).SetValue(this, val);
        }
        public bool search(string s)
        {
            foreach (var item in GetFields())
            {
                string m = Convert.ToString(item);
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
            string[] fields = { "id", "date", "start_time", "end_time", "meeting_url", "owner", "participant" };
            int i = 0;
            foreach (var item in GetFields())
            {
                res += fields[i] + ": " + item + '\n';
                i++;
            }
            return res;
        }
        public string FileFormat()
        {
            string res = "";
            foreach (var item in GetFields())
            {
                res += item + ";";
            }
            res = res.Substring(0, res.Length - 1);
            return res;
        }
    }
}
