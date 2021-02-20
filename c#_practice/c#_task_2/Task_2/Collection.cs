using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Threading.Tasks;
using System.ComponentModel;

namespace Task_2
{
    public static class Ids
    {
        public static List<string> unique = new List<string>();
    }
    public class Collection<T>
    {
        List<T> li;
        int size;
        BindingFlags bindingFlags = BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public;
        public Collection()
        {
            li = new List<T>();
            size = 0;
        }

        public void AddTo(T obj, string file_name)
        {
            li.Add(obj);
            Type o = obj.GetType();  
            var a = o.GetField("id", bindingFlags).GetValue(obj).ToString();
            if (Ids.unique.Contains(a.ToString()))
            {
                Console.WriteLine("Id is not unique!");
                return;
            }
            Ids.unique.Add(a.ToString());
            if (file_name != "None") { RewriteFile(file_name); }
            size++;
        }

        public void Remove(string id, string file_name)
        {
            for (int i = 0; i < size; i++)
            {
                Type obj = li[i].GetType();
                var a = obj.GetField("id", bindingFlags).GetValue(li[i]).ToString();
                if (a.Equals(id))
                {
                    li.Remove(li[i]);
                    Ids.unique.Remove(id);
                    RewriteFile(file_name);
                    size--;
                    return;
                }
            }
        }
        public void Edit(string id, string field, string file_name)
        {
            Type type = typeof(T);
            PropertyInfo prop = type.GetProperty(field);
            if (field.ToLower() == "id")
            {
                Console.WriteLine("You can't change id!");
                return;
            }
            Console.WriteLine("Type new value for the field");
            string new_value = Console.ReadLine();
            for (int i = 0; i < size; i++)
            {
                Type obj = li[i].GetType();
                var a = obj.GetField("id", bindingFlags).GetValue(li[i]).ToString();
                if (a.Equals(id))
                {
                    try { prop.SetValue(li[i], Convert.ChangeType(new_value, prop.PropertyType)); }
                    catch
                    {
                        Console.WriteLine("Field or value are wrong");
                        return;
                    }
                    RewriteFile(file_name);
                }
            }
        }

        public void Sort(string param)
        {
            try { li = li.OrderBy(obj => obj.GetType().GetProperty(param).GetValue(obj, null)).ToList(); }
            catch
            {
                Console.WriteLine("No such field");
            }
        }

        public void RewriteFile(string file)
        {
            File.WriteAllText(file, string.Empty);
            foreach (T obj in li)
            {
                string res = obj.ToString();
                using (StreamWriter sw = File.AppendText(file))
                {
                    sw.WriteLine(res);
                }
            }
        }

        public void Search(string val)
        {
            for (int i = 0; i < size; i++)
            {
                bool b = false;
                PropertyInfo[] props = li[i].GetType().GetProperties();
                foreach (var item in props)
                {
                    string m = Convert.ToString(item.GetValue(li[i]));
                    if (m.Contains(val))
                    {
                        b = true;
                        break; 
                    }
                }
                if (b) { Console.WriteLine(li[i]); }
            }
        }

        public void Print()
        {
            foreach (T i in li)
            {
                Console.WriteLine(i);
            }
        }
    }
}