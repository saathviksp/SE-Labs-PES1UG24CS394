# Peer-to-Peer Carpooling & Expense Splitter
## UML Use-Case Diagram Specification - Lab 1

**System Boundary Label:** Peer-to-Peer Carpooling & Expense Splitter  
**Actors:**
* **Rider Commuter:** Primary actor seeking a shared ride along daily commute routes.
* **Driver Host:** Primary actor offering vehicle seats to split travel costs.
* **Map & Route Service:** External system supporting actor providing route calculations and detour distance evaluation.

---

### 1. Diagram Preview

![UML Use-Case Diagram](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.png)

* **Editable Diagram Source File:** [`use-case-diagram.drawio`](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.drawio)
* **High-Resolution Submission Image:** [`use-case-diagram.png`](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.png)
* **PDF Submission Document:** [`use-case-diagram.pdf`](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.pdf)

---

### 2. Use Case Inventory

| Use Case ID | Use Case Name | Primary Actor(s) | Description |
| :--- | :--- | :--- | :--- |
| **UC-01** | Register / Login | Rider Commuter, Driver Host | Authenticate users and grant access to portal services. |
| **UC-02** | Create Driver Profile | Driver Host | Set up vehicle details and host profile settings. |
| **UC-03** | Verify Driver / Vehicle | System / Driver Host | Verify driving license and vehicle registration documents. |
| **UC-04** | Set Commute Route | Rider Commuter, Driver Host | Define origin, destination, and key route waypoints. |
| **UC-05** | Set Daily Schedule | Rider Commuter, Driver Host | Configure recurring daily departure time windows. |
| **UC-06** | Search Carpool Matches | Rider Commuter | Search for drivers with overlapping commute routes. |
| **UC-07** | Calc Route Compatibility | Map & Route Service, System | Compute route overlap enforcing the 1.5 km detour threshold. |
| **UC-08** | View Matched Rides | Rider Commuter | Display sorted list of compatible carpool matches. |
| **UC-09** | Request a Ride | Rider Commuter | Send seat reservation request to a driver host. |
| **UC-10** | Approve / Reject Request | Driver Host | Review incoming passenger requests and accept/decline. |
| **UC-11** | Calc Fuel Cost Share | System | Compute proportional cost share split per passenger. |
| **UC-12** | View / Manage Bookings | Rider Commuter, Driver Host | Track active, upcoming, and completed ride bookings. |
| **UC-13** | Rate Ride / User | Rider Commuter, Driver Host | Submit rating and performance feedback post-trip. |

---

### 3. UML Relationship Specification

#### `<<include>>` Relationships (Points FROM Base Use Case TO Included Use Case)
1. **`UC-02: Create Driver Profile` $\xrightarrow{<<include>>}$ `UC-03: Verify Driver / Vehicle`**
   * *Base Use Case:* `UC-02: Create Driver Profile`
   * *Included Use Case:* `UC-03: Verify Driver / Vehicle`
   * *Rationale:* Creating a driver profile mandatorily includes identity and vehicle document verification.

2. **`UC-06: Search Carpool Matches` $\xrightarrow{<<include>>}$ `UC-07: Calc Route Compatibility`**
   * *Base Use Case:* `UC-06: Search Carpool Matches`
   * *Included Use Case:* `UC-07: Calc Route Compatibility`
   * *Rationale:* Searching for carpool matches automatically triggers the route compatibility calculation.

3. **`UC-09: Request a Ride` $\xrightarrow{<<include>>}$ `UC-11: Calc Fuel Cost Share`**
   * *Base Use Case:* `UC-09: Request a Ride`
   * *Included Use Case:* `UC-11: Calc Fuel Cost Share`
   * *Rationale:* Requesting a ride automatically calculates the estimated fuel cost split.

---

#### `<<extend>>` Relationship (Points FROM Extending Use Case TO Base Use Case)
1. **`UC-13: Rate Ride / User` $\xrightarrow{<<extend>>}$ `UC-12: View / Manage Bookings`**
   * *Extending Use Case:* `UC-13: Rate Ride / User`
   * *Base Use Case:* `UC-12: View / Manage Bookings`
   * *Rationale:* Rating a ride/user optionally extends booking management after a ride is completed.
