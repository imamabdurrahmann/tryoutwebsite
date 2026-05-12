[Setup]
AppName=Tryout CPNS
AppVersion=1.0.0
AppPublisher=Tryout CPNS
DefaultDirName={autopf}\TryoutCPNS
DefaultGroupName=Tryout CPNS
OutputDir=installer
OutputBaseFilename=TryoutCPNS-Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
WizardImageFile=assets\logo\icon_256.png
SetupIconFile=assets\logo\app_icon.ico
UninstallDisplayIcon={app}\tryout_cpns.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Buat shortcut di Desktop"; GroupDescription: "Ikon shortcut:"
Name: "quicklaunchicon"; Description: "Buat shortcut di Quick Launch"; GroupDescription: "Ikon shortcut:"; OnlyBelowVersion: 6.1; Flags: unchecked

[Files]
Source: "build\windows\x64\runner\Release\tryout_cpns.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\windows\x64\runner\Release\flutter_windows.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\windows\x64\runner\Release\dartjni.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\windows\x64\runner\Release\screen_retriever_windows_plugin.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\windows\x64\runner\Release\window_manager_plugin.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\windows\x64\runner\Release\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Tryout CPNS"; Filename: "{app}\tryout_cpns.exe"
Name: "{group}\Uninstall Tryout CPNS"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Tryout CPNS"; Filename: "{app}\tryout_cpns.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Tryout CPNS"; Filename: "{app}\tryout_cpns.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\tryout_cpns.exe"; Description: "Jalankan Tryout CPNS"; Flags: nowait postinstall skipifsilent

[Code]
procedure InitializeWizard;
begin
  WizardForm.WelcomeLabel2.Caption := 'Installer ini akan installing aplikasi Tryout CPNS di komputer Anda.' + #13#10 + #13#10 +
  'Klik "Install" untuk melanjutkan, atau "Batal" untuk membatalkan.';
end;