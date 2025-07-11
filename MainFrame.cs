using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace Similar_v2
{
    public partial class MainFrame : Form
    {
        // private Button openButton;
        private RoundedTextBox playlistBox;

        public MainFrame()
        {
            this.Text = "Main Form";
            this.Width = 1280;
            this.Height = 720;

            this.StartPosition = FormStartPosition.CenterScreen;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = System.Drawing.ColorTranslator.FromHtml("#4A94D4");


            playlistBox = new RoundedTextBox();
            playlistBox.Multiline = true;
            playlistBox.Font = new System.Drawing.Font("Segoe UI", playlistBox.Height * 1f);
            playlistBox.Location = new System.Drawing.Point(20, 50);
            playlistBox.BorderStyle = BorderStyle.None;


            // openButton = new Button();
            // openButton.Text = "Open Second Form";
            // openButton.Location = new System.Drawing.Point(80, 70);
            // openButton.Click += OpenButton_Click;

            // this.Controls.Add(openButton);
            this.Controls.Add(playlistBox);

            this.Resize += MainFrame_Resize;
        }

        private void OpenButton_Click(object? sender, EventArgs? e)
        {
            PlaylistFrame playlistFrame = new PlaylistFrame();
            playlistFrame.FormClosed += (s, args) => this.Show(); // Show MainFrame again when PlaylistFrame closes
            this.Hide(); // Hide MainFrame
            playlistFrame.Show();
        }

        private void MainFrame_Resize(object? sender, EventArgs? e)
        {   
            playlistBox.Width = (int)(this.ClientSize.Width * 0.34);
            playlistBox.Height = (int)(this.ClientSize.Height * 0.050);
            playlistBox.Location = new System.Drawing.Point(
                (this.ClientSize.Width - playlistBox.Width) / 2,
                playlistBox.Location.Y
            );
        }



        

    }
    
    public class RoundedTextBox : TextBox
    {
        protected override void OnCreateControl()
        {
            base.OnCreateControl();
            SetRoundedRegion();
        }

        protected override void OnResize(EventArgs e)
        {
            base.OnResize(e);
            SetRoundedRegion();
        }

        private void SetRoundedRegion()
        {
            int radius = 15; // Change for more/less roundness
            var path = new GraphicsPath();
            path.AddArc(0, 0, radius, radius, 180, 90);
            path.AddArc(this.Width - radius, 0, radius, radius, 270, 90);
            path.AddArc(this.Width - radius, this.Height - radius, radius, radius, 0, 90);
            path.AddArc(0, this.Height - radius, radius, radius, 90, 90);
            path.CloseAllFigures();
            this.Region = new Region(path);
        }
    }

    public class RoundedPanel : Panel
    {
        protected override void OnPaint(PaintEventArgs e)
        {
            int radius = 15;
            var path = new GraphicsPath();
            path.AddArc(0, 0, radius, radius, 180, 90);
            path.AddArc(this.Width - radius, 0, radius, radius, 270, 90);
            path.AddArc(this.Width - radius, this.Height - radius, radius, radius, 0, 90);
            path.AddArc(0, this.Height - radius, radius, radius, 90, 90);
            path.CloseAllFigures();

            this.Region = new Region(path);
            using (var brush = new SolidBrush(this.BackColor))
            {
                e.Graphics.FillPath(brush, path);
            }
            base.OnPaint(e);
        }
    }
}
