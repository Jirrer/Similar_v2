using System.Windows.Forms;

namespace Similar_v2
{
    public class PlaylistFrame : Form
    {
        public PlaylistFrame()
        {
            this.Text = "Second Form";
            this.Width = 250;
            this.Height = 150;

            Label label = new Label();
            label.Text = "Hello from the second form!";
            label.AutoSize = true;
            label.Location = new System.Drawing.Point(40, 50);

            this.Controls.Add(label);
        }
    }
}
