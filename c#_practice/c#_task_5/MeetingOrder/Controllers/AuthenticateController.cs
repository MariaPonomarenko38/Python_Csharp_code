using MeetingOrder.Authentication;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using System.Threading.Tasks;

namespace MeetingOrder.Authentication
{
    /// <summary>
    /// Authentication Controller
    /// </summary>
    [Route("api/User")]
    [ApiController]
    public class AuthenticateController : ControllerBase
    {
        private readonly UserManager<ApplicationUser> userManager;
        private readonly RoleManager<IdentityRole> roleManager;
        private readonly IConfiguration _configuration;
        /// <summary>
        /// Authentication Controller
        /// </summary>
        public AuthenticateController(UserManager<ApplicationUser> userManager, RoleManager<IdentityRole> roleManager, IConfiguration configuration)
        {
            this.userManager = userManager;
            this.roleManager = roleManager;
            _configuration = configuration;
        }
        /// <summary>
        /// This POST method is responsible for login
        /// </summary>
        /// <returns>Token</returns>
        [HttpPost]
        [Route("login")]
        public async Task<IActionResult> Login([FromBody] LoginModel model)
        {
            var user = await userManager.FindByEmailAsync(model.Email);
            if (user != null && await userManager.CheckPasswordAsync(user, model.Password))
            {
                var userRoles = await userManager.GetRolesAsync(user);

                var authClaims = new List<Claim>
            {
                new Claim(ClaimTypes.Name, user.Email),
                new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()),
            };

                foreach (var userRole in userRoles)
                {
                    authClaims.Add(new Claim(ClaimTypes.Role, userRole));
                }

                var authSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["JWT:Secret"]));

                var token = new JwtSecurityToken(
                    issuer: _configuration["JWT:ValidIssuer"],
                    audience: _configuration["JWT:ValidAudience"],
                    expires: DateTime.Now.AddHours(3),
                    claims: authClaims,
                    signingCredentials: new SigningCredentials(authSigningKey, SecurityAlgorithms.HmacSha256)
                    );

                return Ok(new
                {
                    token = new JwtSecurityTokenHandler().WriteToken(token),
                    expiration = token.ValidTo
                });
            }
            return Unauthorized();
        }
        /// <summary>
        /// This POST method registers new user
        /// </summary>
        /// <response code="500">If user with given email already exists</response>
        [HttpPost]
        public async Task<IActionResult> Register([FromBody] RegisterModel model)
        {
            if (!await roleManager.RoleExistsAsync(UserRoles.Admin.ToString()))
                await roleManager.CreateAsync(new IdentityRole(UserRoles.Admin.ToString()));
            if (!await roleManager.RoleExistsAsync(UserRoles.User.ToString()))
                await roleManager.CreateAsync(new IdentityRole(UserRoles.User.ToString()));
            var userExists = await userManager.FindByEmailAsync(model.Email);
            if (userExists != null)
                return StatusCode(StatusCodes.Status500InternalServerError, new Responce { Status = "Error", Message = "User already exists!" });

            ApplicationUser user = new ApplicationUser()
            {
                Email = model.Email,
                SecurityStamp = Guid.NewGuid().ToString(),
                UserName = model.Email
            };
            var result = await userManager.CreateAsync(user, model.Password);
            if (!result.Succeeded)
            {
                return StatusCode(StatusCodes.Status500InternalServerError, new Responce { Status = result.ToString(), Message = "User creation failed! Please check user details and try again." });
            }
            //if (model.Role == "Admin")
            //{
            //    if (!await roleManager.RoleExistsAsync(UserRoles.Admin))
            //        await roleManager.CreateAsync(new IdentityRole(UserRoles.Admin));
            //    if (!await roleManager.RoleExistsAsync(UserRoles.User))
            //        await roleManager.CreateAsync(new IdentityRole(UserRoles.User));
            //    if (await roleManager.RoleExistsAsync(UserRoles.Admin))
            //    {
            //        await userManager.AddToRoleAsync(user, UserRoles.Admin);
            //    }
            //}
            return Ok(new Responce { Status = "Success", Message = "User created successfully!" });
        }
    }
}
