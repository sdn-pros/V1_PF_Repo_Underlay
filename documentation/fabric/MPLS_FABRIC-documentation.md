# MPLS_FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| MPLS_FABRIC | p | P1 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | p | P2 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | p | P3 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | p | P4 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | p | P5 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | p | P6 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | pe | PE1 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | pe | PE2 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | pe | PE3 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | pe | PE4 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | rr | RR5 | - | vEOS-lab | Provisioned | - |
| MPLS_FABRIC | rr | RR6 | - | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| p | P1 | e1 | p | P5 | e2 |
| p | P1 | e2 | pe | PE1 | e2 |
| p | P1 | e3 | pe | PE2 | e2 |
| p | P1 | e4 | p | P6 | e4 |
| p | P2 | e1 | p | P6 | e2 |
| p | P2 | e2 | pe | PE1 | e3 |
| p | P2 | e3 | pe | PE2 | e3 |
| p | P2 | e4 | p | P5 | e4 |
| p | P3 | e1 | p | P5 | e3 |
| p | P3 | e2 | pe | PE3 | e2 |
| p | P3 | e3 | pe | PE4 | e2 |
| p | P3 | e4 | p | P6 | e5 |
| p | P4 | e1 | p | P6 | e3 |
| p | P4 | e2 | pe | PE3 | e3 |
| p | P4 | e3 | pe | PE4 | e3 |
| p | P4 | e4 | p | P5 | e5 |
| p | P5 | e1 | p | P6 | e1 |
| pe | PE1 | e1 | pe | PE2 | e1 |
| pe | PE1 | e6 | rr | RR5 | e6 |
| pe | PE1 | e8 | rr | RR6 | e10 |
| pe | PE2 | e6 | rr | RR5 | e7 |
| pe | PE2 | e8 | rr | RR6 | e13 |
| pe | PE3 | e1 | pe | PE4 | e1 |
| pe | PE3 | e6 | rr | RR6 | e6 |
| pe | PE3 | e8 | rr | RR5 | e10 |
| pe | PE4 | e6 | rr | RR6 | e7 |
| pe | PE4 | e8 | rr | RR5 | e13 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| P1 | e1 | 192.168.102.18/31 | P5 | e2 | 192.168.102.19/31 |
| P1 | e2 | 192.168.102.1/31 | PE1 | e2 | 192.168.102.0/31 |
| P1 | e3 | 192.168.102.5/31 | PE2 | e2 | 192.168.102.4/31 |
| P1 | e4 | 192.168.102.20/31 | P6 | e4 | 192.168.102.21/31 |
| P2 | e1 | 192.168.102.26/31 | P6 | e2 | 192.168.102.27/31 |
| P2 | e2 | 192.168.102.3/31 | PE1 | e3 | 192.168.102.2/31 |
| P2 | e3 | 192.168.102.7/31 | PE2 | e3 | 192.168.102.6/31 |
| P2 | e4 | 192.168.102.24/31 | P5 | e4 | 192.168.102.25/31 |
| P3 | e1 | 192.168.102.31/31 | P5 | e3 | 192.168.102.30/31 |
| P3 | e2 | 192.168.102.36/31 | PE3 | e2 | 192.168.102.37/31 |
| P3 | e3 | 192.168.102.38/31 | PE4 | e2 | 192.168.102.39/31 |
| P3 | e4 | 192.168.102.33/31 | P6 | e5 | 192.168.102.32/31 |
| P4 | e1 | 192.168.102.35/31 | P6 | e3 | 192.168.102.34/31 |
| P4 | e2 | 192.168.102.40/31 | PE3 | e3 | 192.168.102.41/31 |
| P4 | e3 | 192.168.102.42/31 | PE4 | e3 | 192.168.102.43/31 |
| P4 | e4 | 192.168.102.33/31 | P5 | e5 | 192.168.102.32/31 |
| P5 | e1 | 192.168.102.28/31 | P6 | e1 | 192.168.102.29/31 |
| PE1 | e1 | 192.168.102.8/31 | PE2 | e1 | 192.168.102.9/31 |
| PE1 | e6 | 192.168.102.10/31 | RR5 | e6 | 192.168.102.11/31 |
| PE1 | e8 | 192.168.102.12/31 | RR6 | e10 | 192.168.102.13/31 |
| PE2 | e6 | 192.168.102.14/31 | RR5 | e7 | 192.168.102.15/31 |
| PE2 | e8 | 192.168.102.16/31 | RR6 | e13 | 192.168.102.17/31 |
| PE3 | e1 | 192.168.102.44/31 | PE4 | e1 | 192.168.102.45/31 |
| PE3 | e6 | 192.168.102.48/31 | RR6 | e6 | 192.168.102.49/31 |
| PE3 | e8 | 192.168.102.46/31 | RR5 | e10 | 192.168.102.47/31 |
| PE4 | e6 | 192.168.102.52/31 | RR6 | e7 | 192.168.102.53/31 |
| PE4 | e8 | 192.168.102.50/31 | RR5 | e13 | 192.168.102.51/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 12 | 4.69 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| MPLS_FABRIC | P1 | 192.168.101.1/32 |
| MPLS_FABRIC | P2 | 192.168.101.2/32 |
| MPLS_FABRIC | P3 | 192.168.101.3/32 |
| MPLS_FABRIC | P4 | 192.168.101.4/32 |
| MPLS_FABRIC | P5 | 192.168.101.5/32 |
| MPLS_FABRIC | P6 | 192.168.101.6/32 |
| MPLS_FABRIC | PE1 | 192.168.101.21/32 |
| MPLS_FABRIC | PE2 | 192.168.101.22/32 |
| MPLS_FABRIC | PE3 | 192.168.101.23/32 |
| MPLS_FABRIC | PE4 | 192.168.101.24/32 |
| MPLS_FABRIC | RR5 | 192.168.101.35/32 |
| MPLS_FABRIC | RR6 | 192.168.101.36/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| MPLS_FABRIC | P1 | 49.0001.0000.0001.0001.00 |
| MPLS_FABRIC | P2 | 49.0001.0000.0001.0002.00 |
| MPLS_FABRIC | P3 | 49.0001.0000.0001.0003.00 |
| MPLS_FABRIC | P4 | 49.0001.0000.0001.0004.00 |
| MPLS_FABRIC | P5 | 49.0001.0000.0001.0005.00 |
| MPLS_FABRIC | P6 | 49.0001.0000.0001.0006.00 |
| MPLS_FABRIC | PE1 | 49.0001.0000.0001.0021.00 |
| MPLS_FABRIC | PE2 | 49.0001.0000.0001.0022.00 |
| MPLS_FABRIC | PE3 | 49.0001.0000.0001.0023.00 |
| MPLS_FABRIC | PE4 | 49.0001.0000.0001.0024.00 |
| MPLS_FABRIC | RR5 | 49.0001.0000.0001.0035.00 |
| MPLS_FABRIC | RR6 | 49.0001.0000.0001.0036.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
