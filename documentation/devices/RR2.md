# RR2

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
| Ethernet1 | - | routed | - | 192.71.72.2/24 | default | 1500 | True | - | - |
| Ethernet2 | - | routed | - | 192.15.72.2/24 | default | 1500 | False | - | - |
| Ethernet3 | - | routed | - | 192.16.72.2/24 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   shutdown
   mtu 1500
   no switchport
   ip address 192.71.72.2/24
!
interface Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 192.15.72.2/24
!
interface Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 192.16.72.2/24
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Dps1 | - | default | 72.72.72.72/32 |
| Loopback10 | RR2_lo10 | default | 192.168.0.72/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Dps1 | - | default | - |
| Loopback10 | RR2_lo10 | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Dps1
   no shutdown
   ip address 72.72.72.72/32
!
interface Loopback10
   description RR2_lo10
   no shutdown
   ip address 192.168.0.72/32
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
| 65000 | 192.168.0.72 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.15.72.1 | 65102 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.16.72.1 | 65103 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 192.168.0.72
   neighbor 192.15.72.1 remote-as 65102
   neighbor 192.15.72.1 allowas-in 6
   neighbor 192.16.72.1 remote-as 65103
   neighbor 192.16.72.1 allowas-in 6
   !
   address-family ipv4
      neighbor 192.15.72.1 activate
      neighbor 192.16.72.1 activate
      network 192.168.0.72/32
      redistribute connected
```
