Add-Type -AssemblyName System.Windows.Forms

for ($i=0; $i -lt 10; $i++) {
    [System.Windows.Forms.MessageBox]::Show(
        "Do you believe in the multiverse or donkeys?",
        "Question",
        [System.Windows.Forms.MessageBoxButtons]::YesNo,
        [System.Windows.Forms.MessageBoxIcon]::Question,
        [System.Windows.Forms.MessageBoxDefaultButton]::Button1,
        [System.Windows.Forms.MessageBoxOptions]::ServiceNotification
    )
}