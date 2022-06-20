# Instalación:

```bash
$ apt update
$ apt install mingw-w64
$ curl https://sliver.sh/install|sudo bash
```
Una vez instalado se inicializa la herramienta. 

```bash
$ sliver
```
# Comandos básicos:

## Ayuda

El comando para mostrar la ayuda es naturalmente help. 

```bash
sliver > help

Commands:
=========
  clear       clear the screen
  exit        exit the shell
  help        use 'help [command]' for command help
  monitor     Monitor threat intel platforms for Sliver implants
  wg-config   Generate a new WireGuard client config
  wg-portfwd  List ports forwarded by the WireGuard tun interface
  wg-socks    List socks servers listening on the WireGuard tun interface


Generic:
========
  aliases           List current aliases
  armory            Automatically download and install extensions/aliases
  background        Background an active session
  beacons           Manage beacons
  canaries          List previously generated canaries
  dns               Start a DNS listener
  env               List environment variables
  generate          Generate an implant binary
  hosts             Manage the database of hosts
  http              Start an HTTP listener
  https             Start an HTTPS listener
  implants          List implant builds
  jobs              Job control
  licenses          Open source licenses
  loot              Manage the server's loot store
  mtls              Start an mTLS listener
  prelude-operator  Manage connection to Prelude's Operator
  profiles          List existing profiles
  reaction          Manage automatic reactions to events
  regenerate        Regenerate an implant
  sessions          Session management
  settings          Manage client settings
  stage-listener    Start a stager listener
  tasks             Beacon task management
  update            Check for updates
  use               Switch the active session or beacon
  version           Display version information
  websites          Host static content (used with HTTP C2)
  wg                Start a WireGuard listener


Multiplayer:
============
  operators  Manage operators

```
Para conocer el detalle de un comando en particular se debe usar `help comando` como se ve a continuación:

```bash
sliver > help http

Start an HTTP listener

Usage:
======
  http [flags]

Flags:
======
  -D, --disable-otp                 disable otp authentication
  -d, --domain            string    limit responses to specific domain
  -h, --help                        display help
  -L, --lhost             string    interface to bind server to
  -J, --long-poll-jitter  string    server-side long poll jitter (default: 2s)
  -T, --long-poll-timeout string    server-side long poll timeout (default: 1s)
  -l, --lport             int       tcp listen port (default: 80)
  -p, --persistent                  make persistent across restarts
  -t, --timeout           int       command timeout in seconds (default: 60)
  -w, --website           string    website name (see websites cmd)

```

La estructura de funcionamiento de sliver es igual a esta:

![Esquema de red de sliver](sliver.png)

#

