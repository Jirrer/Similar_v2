using System.Windows.Forms;

namespace Similar_v2
{
    public class PlaylistFrame : Form
    {
        public PlaylistFrame()
        {
            this.Text = "Similar_v2 - New Playlist";
            this.Width = 1280;
            this.Height = 720;

            this.StartPosition = FormStartPosition.CenterScreen;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = System.Drawing.ColorTranslator.FromHtml("#4A94D4");

        }
    }
}
