## Logitech Exploit install guide

> [!WARNING]
> Do not update the GHUB application as the exploit only works on this version of the application!

> [!WARNING]
> In some games, this exploit is visible as an anti-cheat.

- Download and install [GHUB](https://disk.yandex.ru/d/LagJI9dR-kM9cQ).
- Open `config.ini` and change `mouse_ghub` option to `true`.
- Do not close the application while using the exploit.
- Disable updates in GHUB.
	- Go to path: `C:\Windows\System32\drivers\etc`.
	- Open `hosts` file as admin.
    - Add 2 lines at the end of the file:
		- `127.0.0.1 updates.ghub.logitechg.com`
		- `127.0.0.1 util.logitech.io`