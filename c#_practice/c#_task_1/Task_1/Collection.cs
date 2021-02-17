using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Globalization;
using System.IO;
using System.Threading.Tasks;

namespace Task_1
{
    public class Sorting
    {
        public static String []fields = {"id", "owner", "participant", "start_time", "end_time", "date"};
    }
    public class Collection
    {
        List<OnlineMeeting> li;
        int size;

        public Collection()
        {
            li = new List<OnlineMeeting>();
            size = 0;
        }

        public void FillCollectionFile(string file)
        {
            string[] lines = File.ReadAllLines(file);
            File.WriteAllText(file, string.Empty);
            foreach (string line in lines)
            {
                Validation v = new Validation(line);
                if (v.ValidateAll("add") == true)
                {
                    using (StreamWriter sw = File.AppendText(file))
                    {
                        sw.WriteLine(line);
                        OnlineMeeting obj = new OnlineMeeting(line);
                        li.Add(obj);
                        size++;
                    }
                }
            }
        }
        public void AddTo(string val, string file)
        {
            if (Input.ValidateInput(val, "add") == false)
            {
                Console.WriteLine("Values are incorrect!");
                return;
            }
            OnlineMeeting m = new OnlineMeeting(val);
            li.Add(m);
            size++;
            RewriteFile(file);
        }

        public void Remove(string id, string file)
        {
            foreach (OnlineMeeting i in li)
            {
                if (i.Get("id") == id)
                {
                    li.Remove(i);
                    Id.ids.Remove(id);
                    size--;
                    RewriteFile(file);
                    return;
                }
            }
            Console.WriteLine("No such meeting");
        }

        public void Edit(string id, string val, string file)
        {
            if (Input.ValidateInput(val, "edit") == false)
            {
                Console.WriteLine("Values are incorrect!");
                return;
            }
            String[] arr = val.Split(';');
            if (arr[0] != id)
            {
                Console.WriteLine("You can't change id!");
                return;
            }
            for (int i = 0; i < size; i++)
            {
                if (li[i].Get("id") == id)
                {
                    OnlineMeeting a = new OnlineMeeting(val);
                    li[i] = a;
                    RewriteFile(file);
                    return;
                }
            }
            Console.WriteLine("No such id");
        }


        public bool Compare(string param, OnlineMeeting a, OnlineMeeting b)
        {
            string x = a.Get(param);
            string y = b.Get(param);
            if (param == "owner" || param == "participant")
            {
                x = x.ToLower(new CultureInfo("en-US", false));
                y = y.ToLower(new CultureInfo("en-US", false));
                return String.Compare(x, y) > 0;
            }
            else if (param == "start_time" || param == "end_time" || param == "date")
            {
                DateTime d = DateTime.Parse(x);
                DateTime d1 = DateTime.Parse(y);
                return DateTime.Compare(d, d1) > 0;
            }
            else if (param == "id")
            {
                return Int32.Parse(x) > Int32.Parse(y);
            }
            else
            {
                return true;
            }
        }

        public void Sort(string param)
        {
            if (Sorting.fields.Contains(param) == false)
            {
                Console.WriteLine("Can't sort by this parametr");
                return;
            }
            for (int i = 0; i < size - 1; i++)
            {
                for (int j = 0; j < size - i - 1; j++)
                {
                    if (Compare(param, li[j], li[j + 1]))
                    {
                        OnlineMeeting tmp = li[j];
                        li[j] = li[j + 1];
                        li[j + 1] = tmp;
                    }
                }
            }
        }

        public void RewriteFile(string file)
        {
            File.WriteAllText(file, string.Empty);
            foreach (OnlineMeeting obj in li)
            {
                using (StreamWriter sw = File.AppendText(file))
                {
                    sw.WriteLine(obj.FileFormat());
                }
            }
        }

        public void Search(string val)
        {
            foreach (OnlineMeeting i in li)
            {
                if (i.search(val))
                {
                    Console.WriteLine(i);
                }
            }
        }

        public void Print()
        {
            foreach (OnlineMeeting i in li)
            {
                Console.WriteLine(i);
            }
        }
    }
}
