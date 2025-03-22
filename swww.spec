%global debug_package %{nil}

%global bitcode_commit 5f25a59be3e66deef721e7eb2369deb1aa32d263
%global bitcode_shortcommit %(c=%{bitcode_commit}; echo ${c:0:7})

Name:		swww
Version:	0.9.5
Release:	1
URL:		https://github.com/LGFae/swww
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    swww-cargo-vendor-0.9.5.tar.xz
Source2:    cargo_config
Source100:  pack-cargo-vendor.sh
Summary:	A Solution to your Wayland Wallpaper Woes
License:	GPL-3.0
Group:		Wayland/Utils

BuildRequires:	cargo
BuildRequires: scdoc
BuildRequires: pkgconfig(liblz4)

%description
%summary

%prep
%autosetup -n %{name}-%{version} -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
cargo build --release --verbose
./doc/gen.sh

%install
install -Dpm755 target/release/swww %{buildroot}%{_bindir}/swww
install -Dpm755 target/release/swww-daemon %{buildroot}%{_bindir}/swww-daemon
install -Dpm644 ./doc/generated/*.1 -t %{buildroot}%{_mandir}/man1
install -Dpm644 completions/_swww %{buildroot}/%{_datadir}/zsh-completions/completions/%{name}
install -Dpm644 completions/swww.bash %{buildroot}/%{_datadir}/bash-completions/completions/%{name}
install -Dpm644 completions/swww.fish %{buildroot}/%{_datadir}/fish-completions/completions/%{name}.fish

%files
%license LICENSE
%doc README.md
%{_bindir}/swww
%{_bindir}/swww-daemon
%{_mandir}/man1/swww*.1.*
%{_datadir}/zsh-completions/completions/%{name}
%{_datadir}/fish-completions/completions/%{name}.fish
%{_datadir}/bash-completions/completions/%{name}
