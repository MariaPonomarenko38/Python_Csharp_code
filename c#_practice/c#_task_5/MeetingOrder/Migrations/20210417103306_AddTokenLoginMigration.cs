using Microsoft.EntityFrameworkCore.Migrations;

namespace MeetingOrder.Migrations
{
    public partial class AddTokenLoginMigration : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "token_login",
                columns: table => new
                {
                    Id = table.Column<string>(nullable: false),
                    UserEmail = table.Column<string>(nullable: true),
                    Token = table.Column<string>(nullable: true),
                    TokenExpDate = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_token_login", x => x.Id);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "token_login");
        }
    }
}
