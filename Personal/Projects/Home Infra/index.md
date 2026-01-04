# Home Infrastructure Documentation

← [Back to Repository](../README.md)

## Overview

This is the complete documentation for a Swarm-managed home infrastructure serving a 17,000 sq ft estate. The platform powers security, environmental, media and R&D workloads using open-source tools with energy-aware design principles.

### Mission Statement

Build a reproducible, fully‑documented infrastructure that:
- Powers critical home automation and security systems
- Provides a teaching lab environment for learning modern DevOps practices
- Maintains 99.9% uptime through redundancy and battery backup
- Scales from 6 hosts to 20+ hosts as needs evolve
- Documents every decision for knowledge transfer

All knowledge will be published (no secrets) before **1 September 2025**.

## Quick Navigation

### Physical Infrastructure
- [Power Systems](01_physical/power.md) - Electrical distribution, meters, and backup systems
- [Room Layout](01_physical/rooms.md) - Physical locations and infrastructure placement
- [Host Mapping](01_physical/host-map.md) - Which hosts live where with UPS assignments

### Network Architecture
- [Network Infrastructure](02_network/infrastructure.md) - Unifi devices, switches, and topology
- [VLANs & DNS](02_network/vlan-dns.md) - Complete VLAN schema and domain structure
- [WAN & NTP](02_network/wan-ntp.md) - Dual-WAN setup, failover, and time synchronization
- [WiFi Networks](02_network/wifi.md) - SSID configuration and guest portal

### Compute & Storage
- [Host Configuration](03_compute-storage/hosts.md) - Hardware specs and role assignments
- [Local Storage](03_compute-storage/storage-local.md) - NVMe RAID and `/data` layout
- [NAS & NFS](03_compute-storage/nas-nfs.md) - Synology configuration and mount points

### Software Stack
- [Version Matrix](04_software-stack/versions.md) - Target versions for all components
- [Stack Overview](04_software-stack/stacks-overview.md) - High-level service architecture
- [Individual Stacks](04_software-stack/) - Detailed documentation per service

### DevOps & Operations
- [Swarm Operations](05_devops/swarm-ops.md) - Direct SSH workflows and command reference
- [Legacy Ansible](05_devops/ansible.md) - Historical inventory schema (read-only)
- [CI/CD](05_devops/ci-cd.md) - GitHub Actions workflows and testing
- [Backup & DR](05_devops/backup-dr.md) - Backup strategy and disaster recovery
- [Monitoring](05_devops/monitoring.md) - Prometheus, Grafana, and alerting

### Security
- [Secrets Management](06_security/secrets.md) - SOPS/Age encryption and key management
- [Network Hardening](06_security/network-hardening.md) - VLAN ACLs and VPN configuration
- [Compliance](06_security/compliance.md) - What data leaves the property

### Operational Runbooks
- [Replace Disk](07_runbooks/replace-disk.md) - Hardware replacement procedures
- [Migrate Stack](07_runbooks/migrate-stack.md) - Moving services between hosts
- [Power Outage](07_runbooks/power-outage.md) - Emergency procedures and recovery

### Reference
- [Glossary](08_glossary.md) - Terms, acronyms, and definitions

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|------------|---------|
| **OS** | Ubuntu 24.04 LTS | Host operating system |
| **Orchestration** | Docker Swarm | Container scheduling and clustering |
| **Configuration** | SSH + Docker Swarm commands | Direct operator runbooks |
| **Networking** | Unifi UDM-Pro | VLAN-aware SDN management |
| **Storage** | Local NVMe + Synology NAS | High-performance local + shared storage |
| **Monitoring** | Prometheus + Grafana + Loki | Observability and alerting |
| **Secrets** | SOPS + Age | Encrypted secrets in Git |
| **Backup** | Restic + NFS | Automated backup and rotation |

## Core Design Principles

- **Idempotency & Repeatability** – Every change is declarative and reversible
- **Energy‑Aware Design** – Critical loads survive ≥ 2 hour grid outages
- **Open‑Source First** – Favor community projects to avoid vendor lock-in
- **Security‑First Architecture** – Least-privilege access, encrypted secrets, TLS everywhere
- **Documentation as Code** – Every configuration decision is documented and version controlled

## Getting Started

1. **New Contributor**: Start with [Host Configuration](03_compute-storage/hosts.md) to understand the hardware layout
2. **Operations**: Jump to [Runbooks](07_runbooks/) for common procedures
3. **Development**: Check [CI/CD](05_devops/ci-cd.md) for testing and deployment workflows
4. **Architecture**: Review [Version Matrix](04_software-stack/versions.md) and [Stack Overview](04_software-stack/stacks-overview.md)

---

*This documentation is maintained as code. Submit pull requests for any corrections or improvements.*
