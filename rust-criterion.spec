# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate criterion

Name:           rust-criterion
Version:        0.5.1
Release:        %autorelease
Summary:        Statistics-driven micro-benchmarking library

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/criterion
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
Patch:          criterion-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Statistics-driven micro-benchmarking library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-devel %{_description}

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%files       -n %{name}+async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-devel %{_description}

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%files       -n %{name}+async-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async_futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async_futures-devel %{_description}

This package contains library source intended for building other packages which
use the "async_futures" feature of the "%{crate}" crate.

%files       -n %{name}+async_futures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async_smol-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async_smol-devel %{_description}

This package contains library source intended for building other packages which
use the "async_smol" feature of the "%{crate}" crate.

%files       -n %{name}+async_smol-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async_std-devel %{_description}

This package contains library source intended for building other packages which
use the "async_std" feature of the "%{crate}" crate.

%files       -n %{name}+async_std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async_tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async_tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "async_tokio" feature of the "%{crate}" crate.

%files       -n %{name}+async_tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cargo_bench_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cargo_bench_support-devel %{_description}

This package contains library source intended for building other packages which
use the "cargo_bench_support" feature of the "%{crate}" crate.

%files       -n %{name}+cargo_bench_support-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+csv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+csv-devel %{_description}

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%files       -n %{name}+csv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+csv_output-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+csv_output-devel %{_description}

This package contains library source intended for building other packages which
use the "csv_output" feature of the "%{crate}" crate.

%files       -n %{name}+csv_output-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+html_reports-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+html_reports-devel %{_description}

This package contains library source intended for building other packages which
use the "html_reports" feature of the "%{crate}" crate.

%files       -n %{name}+html_reports-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+plotters-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+plotters-devel %{_description}

This package contains library source intended for building other packages which
use the "plotters" feature of the "%{crate}" crate.

%files       -n %{name}+plotters-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+real_blackbox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real_blackbox-devel %{_description}

This package contains library source intended for building other packages which
use the "real_blackbox" feature of the "%{crate}" crate.

%files       -n %{name}+real_blackbox-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+smol-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+smol-devel %{_description}

This package contains library source intended for building other packages which
use the "smol" feature of the "%{crate}" crate.

%files       -n %{name}+smol-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+stable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stable-devel %{_description}

This package contains library source intended for building other packages which
use the "stable" feature of the "%{crate}" crate.

%files       -n %{name}+stable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
