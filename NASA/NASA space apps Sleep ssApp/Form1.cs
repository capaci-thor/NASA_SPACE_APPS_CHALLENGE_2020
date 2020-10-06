using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Speech.Synthesis;
using System.Drawing.Text;

namespace NASA_space_apps_Sleep_ssApp
{
    public partial class Form1 : Form
    {


        public Form1()
        {
            InitializeComponent();
           

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            

            this.Show();
            var _ss = new SpeechSynthesizer();

            _ss.SetOutputToDefaultAudioDevice();
            _ss.Speak("Hello");
            _ss.Speak("I am your new assistant ");

            label1.Text = "Welcome \n to the \n international space station";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
