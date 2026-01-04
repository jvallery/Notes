# Power Systems

← [Documentation Index](../index.md)

## Electrical Distribution Overview

The estate operates on 800 AMPs across 4 distinct meters, with future expansion capability to 1600 AMPs. Critical loads are backed by Tesla PowerWall+ systems to maintain operations during grid outages.

| Meter | Panel(s) & Capacity | Back‑up | Primary Loads | Tariff |
|-------|---------------------|---------|---------------|--------|
| Main House | 200 A | 2 × PowerWall+ | House outlets & lighting | 10.45 ¢/kWh |
| Suite | 200 A + 100 A sub (Pool) | 2 × PowerWall+ | Suite outlets & lighting | 10.45 ¢/kWh |
| Pool Pumps & GPU | 200 A | none | Pentair pumps, Compute Rack | 15.16 ¢/kWh |
| Garage/Studio | 200 A | none | EV chargers, heaters, spa | 16.16 ¢/kWh |

## Main Power Infrastructure

- **Power Source**: City of Longmont utility via underground cable
- **Transformer**: Physically located on property, adjacent to all Tesla equipment
- **Current Capacity**: 800 AMPs across 4 distinct meters
- **Future Capacity**: Wiring installed to support up to 1600 AMPs for future expansion
- **Tesla Systems**: PowerWall+ and solar panels are two isolated systems

## Power Yard

Located on the north edge of the property, houses:
- Transformer from city utility
- All Tesla PowerWall+ and solar equipment
- Underground distribution to property sub-panels:
  - Main house (2x panels)
  - Suite (2x panels)
  - Garage (2x panels)
  - Shed
  - Pool mechanical room

## Meter Details

### Meter 1: Main House
- **Panel**: 200 AMP panel in main house
- **Backup**: Connected to 2x PowerWall+ devices and ~25 KW of panels
- **Circuits**: Outlets, lights, etc. in main house
- **Rate**: 10.45¢/kWh (renewable rate) from City of Longmont

### Meter 2: Suite
- **Panel**: 200 AMP panel in main house
- **Backup**: Connected to 2x PowerWall+ devices and ~25 KW of panels
- **Circuits**: Outlets, lights, etc. in suite; includes 100 AMP sub-panel in pool mechanical room
- **Rate**: 10.45¢/kWh (renewable rate) from City of Longmont

### Pool Pumps and GPUs
- **Panel**: Dedicated 200 AMP panel in pool mechanical room
- **Purpose**: Powers swimming pool pumps and feeds basement server rack
- **Rate**: 15.16¢/kWh (non-renewable rate) from City of Longmont

### Garage
- **Panel**: Dedicated 200 AMP panel in suite studio
- **Purpose**: Car chargers, electric heaters, and other non-critical (non-backed up) circuits across garage and suite
- **Rate**: 16.16¢/kWh (non-renewable rate) from City of Longmont

## UPS Systems

| Location | Model | Capacity | Protected Equipment |
|----------|-------|----------|-------------------|
| Server Closet | 3x CyberPower OR500LCDRM1U | 500VA each | Core networking, home1, IoT hubs |
| Compute Rack | CyberPower OR2200LCDRT2U | 2200VA/1320W | GPU workers, home2, NAS |
| Studio | CyberPower OR500LCDRM1U | 500VA | home3, studio networking |

## Energy Design Goals

- **Critical Load Survival**: ≥ 2 hours on UPS power during grid outages
- **PowerWall+ Integration**: Seamless transition during longer outages
- **Load Balancing**: Distribute compute workloads across backed and non-backed circuits
- **Monitoring**: Real-time power consumption tracking via SNMP

---

**Next**: [Room Layout](rooms.md) | **Related**: [Host Mapping](host-map.md)
