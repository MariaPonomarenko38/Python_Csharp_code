using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MeetingOrder.Authentication;
using System.ComponentModel.DataAnnotations.Schema;

namespace MeetingOrder.Models
{
    public class Order
    {
        public string OrderId { get; set; }
        public string ApplicationUserId { get; set; }
        public virtual ApplicationUser ApplicationUser { get; set; }
        public string MeetingId { get; set; }
        public Meeting Meeting { get; set; }
    }
}
