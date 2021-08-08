using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;
using Newtonsoft.Json.Converters;
using System.Runtime.Serialization;

namespace MeetingOrder.Models
{
    public class CustomDateTimeConverter : IsoDateTimeConverter
    {
        public CustomDateTimeConverter()
        {
            DateTimeFormat = "yyyy-MM-dd";
        }

        public CustomDateTimeConverter(string format)
        {
            DateTimeFormat = format;
        }
    }
    public class Meeting : IValidatableObject
    {
        public string MeetingId { get; set; }
        [Required]
        public string Start_time { get; set; }
        [Required]
        public string End_time { get; set; }
        [Required]
        public DateTime Date { get; set; }
        [Required]
        [Url]
        public string Url { get; set; }
        [Required]
        [RegularExpression(@"^[(a-zA-Z)' '(a-zA-Z)]*$",
            ErrorMessage = "Characters are     not allowed.")]
        public string Owner { get; set; }
        [Required]
        [RegularExpression(@"^[(a-zA-Z)' '(a-zA-Z)]*$",
            ErrorMessage = "Characters are not allowed.")]
        public string Participant { get; set; }
        [Required]
        public int Count { get; set; }
        [JsonIgnore] 
        [IgnoreDataMember] 
        public virtual ICollection<Order> Orders { get; set; }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            List<ValidationResult> results = new List<ValidationResult>();
            DateTime dt, dt1;
            if (DateTime.TryParse(Start_time, out dt) == false)
            {
                results.Add(new ValidationResult("Start time wrong", new[] { "Start time" }));
            }
            if (DateTime.TryParse(End_time, out dt1) == false)
            {
                results.Add(new ValidationResult("End time wrong", new[] { "End time" }));
            }
            if (string.Compare(Start_time, End_time) == 1)
            {
                results.Add(new ValidationResult("Time Conflict", new[] { "Time" }));
            }
            return results;
        }
    }
}
