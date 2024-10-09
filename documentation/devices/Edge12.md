# Edge12

## Table of Contents

- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router OSPF](#router-ospf)
  - [Router BGP](#router-bgp)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

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
| Ethernet1 | - | routed | - | 192.12.32.1/24 | VRF_A | 1500 | False | - | - |
| Ethernet2 | - | routed | - | 192.12.15.1/24 | default | 1500 | False | - | - |
| Ethernet3 | - | routed | - | 192.12.16.1/24 | default | 1500 | False | - | - |
| Ethernet4 | - | routed | - | 192.12.31.1/24 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   no shutdown
   mtu 1500
   no switchport
   vrf VRF_A
   ip address 192.12.32.1/24
   ip ospf network point-to-point
   ip ospf area 0
!
interface Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 192.12.15.1/24
!
interface Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 192.12.16.1/24
!
interface Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.12.31.1/24
   ip ospf network point-to-point
   ip ospf area 0
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback10 | Edge-12_lo10 | default | 192.168.0.12/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback10 | Edge-12_lo10 | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback10
   description Edge-12_lo10
   no shutdown
   ip address 192.168.0.12/32
```

## Routing

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| VRF_A | True |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf VRF_A
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| VRF_A | false |

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 10 | 192.168.0.10 | disabled |- | disabled | default | disabled | disabled | - | - | - | - |

#### Router OSPF Router Redistribution

| Process ID | Source Protocol | Include Leaked | Route Map |
| ---------- | --------------- | -------------- | --------- |
| 10 | bgp | disabled | - |

#### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet1 | 0 | - | True |
| Ethernet4 | 0 | - | True |

#### Router OSPF Device Configuration

```eos
!
router ospf 10 vrf VRF_A
   router-id 192.168.0.10
   redistribute bgp
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65000 | 192.168.0.12 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.12.15.2 | 65102 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |
| 192.12.16.2 | 65103 | default | - | - | - | Allowed, allowed 6 times | - | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| VRF_A | - | ospf<br>connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 192.168.0.12
   neighbor 192.12.15.2 remote-as 65102
   neighbor 192.12.15.2 allowas-in 6
   neighbor 192.12.16.2 remote-as 65103
   neighbor 192.12.16.2 allowas-in 6
   redistribute connected
   !
   address-family ipv4
      neighbor 192.12.15.2 activate
      neighbor 192.12.16.2 activate
      network 172.16.12.0/24
      network 192.168.0.12/32
   !
   vrf VRF_A
      redistribute connected
      redistribute ospf
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| VRF_A | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance VRF_A
```
