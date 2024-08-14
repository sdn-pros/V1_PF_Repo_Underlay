# R1-PE1

## Table of Contents

- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [Router BGP](#router-bgp)

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | - | routed | - | 192.15.51.1/24 | default | 1500 | False | - | - |
| Ethernet2 | - | routed | - | 192.15.52.1/24 | default | 1500 | False | - | - |
| Ethernet3 | - | routed | - | 192.15.71.1/24 | default | 1500 | False | - | - |
| Ethernet4 | - | routed | - | 192.15.72.1/24 | default | 1500 | False | - | - |
| Ethernet5 | - | routed | - | 192.10.15.2/24 | default | 1500 | False | - | - |
| Ethernet6 | - | routed | - | 192.11.15.2/24 | default | 1500 | False | - | - |
| Ethernet7 | - | routed | - | 192.12.15.2/24 | default | 1500 | False | - | - |
| Ethernet8 | - | routed | - | 192.13.15.2/24 | default | 1500 | False | - | - |
| Ethernet9 | - | routed | - | 192.14.15.2/24 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 192.15.51.1/24
!
interface Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 192.15.52.1/24
!
interface Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 192.15.71.1/24
!
interface Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.15.72.1/24
!
interface Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.10.15.2/24
!
interface Ethernet6
   no shutdown
   mtu 1500
   no switchport
   ip address 192.11.15.2/24
!
interface Ethernet7
   no shutdown
   mtu 1500
   no switchport
   ip address 192.12.15.2/24
!
interface Ethernet8
   no shutdown
   mtu 1500
   no switchport
   ip address 192.13.15.2/24
!
interface Ethernet9
   no shutdown
   mtu 1500
   no switchport
   ip address 192.14.15.2/24
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback10 | R2-PE2_lo10 | default | 192.168.0.15/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback10 | R2-PE2_lo10 | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback10
   description R2-PE2_lo10
   no shutdown
   ip address 192.168.0.15/32
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |

#### IP Routing Device Configuration

```eos
!
ip routing
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65102 | 192.168.0.15 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.10.15.1 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.11.15.1 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.12.15.1 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.13.15.1 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.14.15.1 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.15.51.2 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.15.52.2 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.15.71.2 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.15.72.2 | 65000 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65102
   router-id 192.168.0.15
   neighbor 192.10.15.1 remote-as 65000
   neighbor 192.10.15.1 allowas-in 6
   neighbor 192.11.15.1 remote-as 65000
   neighbor 192.11.15.1 allowas-in 6
   neighbor 192.12.15.1 remote-as 65000
   neighbor 192.12.15.1 allowas-in 6
   neighbor 192.13.15.1 remote-as 65000
   neighbor 192.13.15.1 allowas-in 6
   neighbor 192.14.15.1 remote-as 65000
   neighbor 192.14.15.1 allowas-in 6
   neighbor 192.15.51.2 remote-as 65000
   neighbor 192.15.51.2 allowas-in 6
   neighbor 192.15.52.2 remote-as 65000
   neighbor 192.15.52.2 allowas-in 6
   neighbor 192.15.71.2 remote-as 65000
   neighbor 192.15.71.2 allowas-in 6
   neighbor 192.15.72.2 remote-as 65000
   neighbor 192.15.72.2 allowas-in 6
   !
   address-family ipv4
      neighbor 192.10.15.1 activate
      neighbor 192.11.15.1 activate
      neighbor 192.12.15.1 activate
      neighbor 192.13.15.1 activate
      neighbor 192.14.15.1 activate
      neighbor 192.15.51.2 activate
      neighbor 192.15.52.2 activate
      neighbor 192.15.71.2 activate
      neighbor 192.15.72.2 activate
      network 192.168.0.15/32
      redistribute connected
```
