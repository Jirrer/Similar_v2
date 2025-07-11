using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;
using Microsoft.Web.WebView2.WinForms;

namespace Similar_v2
{
    public partial class MainFrame : Form
    {
        private RoundedTextBox playlistBox = new RoundedTextBox();
        private int playlistBoxY = 30;
        private List<Label> songLabels = new List<Label>();
        private Panel scrollPanel = new Panel();

        public MainFrame()
        {
            this.Text = "Smilar - Version 2.0";
            this.Width = 1280;
            this.Height = 720;

            this.StartPosition = FormStartPosition.CenterScreen;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = ColorTranslator.FromHtml("#4A94D4");

            this.Resize += MainFrame_Resize;

            addTextBox();
        }

        private void addTextBox()
        {
            playlistBox = new RoundedTextBox
            {
                Multiline = true,
                BorderStyle = BorderStyle.None
            };

            playlistBox.KeyDown += PlaylistBox_KeyDown;
            this.Controls.Add(playlistBox);

            // Setup the scrollable panel below the textbox
            scrollPanel.Location = new Point(0, playlistBox.Bottom + 10);
            scrollPanel.Size = new Size(this.ClientSize.Width, this.ClientSize.Height - scrollPanel.Location.Y);
            scrollPanel.AutoScroll = true;
            scrollPanel.BackColor = ColorTranslator.FromHtml("#4A94D4");
            this.Controls.Add(scrollPanel);

            MainFrame_Resize(this, EventArgs.Empty); // Trigger initial layout
        }

        private void MainFrame_Resize(object? sender, EventArgs? e)
        {
            if (playlistBox == null) return;

            playlistBox.Width = (int)(this.ClientSize.Width * 0.34);
            playlistBox.Height = (int)(this.ClientSize.Height * 0.050);
            playlistBox.Location = new Point(
                (this.ClientSize.Width - playlistBox.Width) / 2,
                playlistBoxY
            );

            // Adjust font size to fit textbox height
            float fontSize = playlistBox.Height * 0.5f;
            playlistBox.Font = new Font("Segoe UI", fontSize, FontStyle.Regular);

            // Resize and reposition scrollPanel below the textbox
            scrollPanel.Location = new Point(0, playlistBox.Bottom + 10);
            scrollPanel.Size = new Size(this.ClientSize.Width, this.ClientSize.Height - scrollPanel.Location.Y);
            scrollPanel.BackColor = ColorTranslator.FromHtml("#4A94D4");

            if (songLabels.Count > 0)
            {
                float totalWidth = scrollPanel.ClientSize.Width;
                float padding = totalWidth * 0.05f;
                float spacing = totalWidth * 0.05f;
                float labelWidth = (totalWidth - 2 * padding - spacing) / 2;
                int labelHeight = 50;

                for (int i = 0; i < songLabels.Count; i++)
                {
                    Label song = songLabels[i];
                    int row = i / 2;
                    int col = i % 2;

                    int x = (int)(padding + col * (labelWidth + spacing));
                    int y = row * (labelHeight + 10);

                    song.Size = new Size((int)labelWidth, labelHeight);
                    song.Location = new Point(x, y);
                }
            }
        }

        private async void PlaylistBox_KeyDown(object? sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                e.SuppressKeyPress = true; // Prevents newline

                string playlistLink = playlistBox.Text;

                this.Controls.Clear();
                songLabels.Clear();
                addTextBox();

                if (!validId(playlistLink))
                {
                    Console.WriteLine("bad link");
                    return;
                }

                float totalWidth = this.ClientSize.Width;
                float padding = totalWidth * 0.05f;  // 5% padding on left and right
                float spacing = totalWidth * 0.05f;  // 5% spacing between columns
                float labelWidth = (totalWidth - 2 * padding - spacing) / 2;
                int labelHeight = 100;

                string[] songs = {
                    "5UODF6hjIwH2amk9PvZJav",
                    "0wvIGFIgbyz4JNwQhZgTv2",
                    "3cbTV3IZZvSBYVcl0xuZbY",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "5UODF6hjIwH2amk9PvZJav",
                    "0wvIGFIgbyz4JNwQhZgTv2",
                    "3cbTV3IZZvSBYVcl0xuZbY",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "5UODF6hjIwH2amk9PvZJav",
                    "0wvIGFIgbyz4JNwQhZgTv2",
                    "3cbTV3IZZvSBYVcl0xuZbY",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "5UODF6hjIwH2amk9PvZJav",
                    "0wvIGFIgbyz4JNwQhZgTv2",
                    "3cbTV3IZZvSBYVcl0xuZbY",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "5UODF6hjIwH2amk9PvZJav",
                    "0wvIGFIgbyz4JNwQhZgTv2",
                    "3cbTV3IZZvSBYVcl0xuZbY",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "5UODF6hjIwH2amk9PvZJav",
                    "0wvIGFIgbyz4JNwQhZgTv2",
                    "3cbTV3IZZvSBYVcl0xuZbY",
                    "70LcF31zb1H0PyJoS1Sx1r",
                    "70LcF31zb1H0PyJoS1Sx1r"
                };
                
                for (int i = 0; i < 30; i++)
                {
                    int row = i / 2;
                    int col = i % 2;

                    int x = (int)(padding + col * (labelWidth + spacing));
                    int y = row * (labelHeight); // add extra vertical space for iframe height

                    var webView = new WebView2
                    {
                        Size = new Size((int)labelWidth, labelHeight), // iframe + label approx height
                        Location = new Point(x, y),
                        Source = new Uri($"https://open.spotify.com/embed/track/{songs[i]}?utm_source=generator")
                    };

                    scrollPanel.BackColor = ColorTranslator.FromHtml("#4A94D4");
                    scrollPanel.Controls.Add(webView);
                    await webView.EnsureCoreWebView2Async(null);  // Initialize WebView2
                }
            }
        }



        private bool validId(string link)
        {
            return true;
        }

        private void getPlaylist(string playlistLink)
        {
            // Placeholder
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
            int radius = 15;
            var path = new GraphicsPath();
            path.AddArc(0, 0, radius, radius, 180, 90);
            path.AddArc(this.Width - radius, 0, radius, radius, 270, 90);
            path.AddArc(this.Width - radius, this.Height - radius, radius, radius, 0, 90);
            path.AddArc(0, this.Height - radius, radius, radius, 90, 90);
            path.CloseAllFigures();
            this.Region = new Region(path);
        }
    }
}
