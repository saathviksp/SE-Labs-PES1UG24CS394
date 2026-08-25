# Peer-to-Peer Carpooling & Expense Splitter
## UML Use-Case Diagram Specification - Lab 1

**System Boundary Label:** Peer-to-Peer Carpooling & Expense Splitter  
**Primary Actors:**
* **Rider Commuter:** Commuter seeking a shared ride along their daily commute route and paying their calculated fuel share.
* **Driver Host:** Vehicle owner offering excess seats along their daily route to split travel costs.

---

### 1. Diagram Preview

![UML Use-Case Diagram](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.png)

* **Editable Diagram Source File:** [`use-case-diagram.drawio`](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.drawio) (Compatible with Draw.io / app.diagrams.net / VS Code Draw.io extension)
* **High-Resolution Submission Image:** [`use-case-diagram.png`](file:///C:/Users/llath/OneDrive/Desktop/Lab1/use-case-diagram.png)

---

### 2. Included Use Cases Summary

| Use Case Name | Primary Actor(s) | Description |
| :--- | :--- | :--- |
| **Register / Login** | Rider Commuter, Driver Host | Authenticate users and grant access to portal services. |
| **Create Driver Profile** | Driver Host | Set up vehicle details and host profile settings. |
| **Verify Driver / Vehicle** | System / Driver Host | Verify driving license and vehicle registration documents. |
| **Set Commute Route** | Rider Commuter, Driver Host | Define origin, destination, and key route waypoints. |
| **Set Daily Commute Schedule** | Rider Commuter, Driver Host | Configure recurring daily departure time windows. |
| **Search for Carpool Matches** | Rider Commuter | Search for drivers with overlapping routes. |
| **Calculate Route Compatibility** | System | Compute route overlap enforcing the 1.5 km detour threshold. |
| **View Matched Rides** | Rider Commuter | Display sorted list of compatible carpool matches. |
| **Request a Ride** | Rider Commuter | Send seat reservation request to a driver host. |
| **Approve / Reject Ride Request** | Driver Host | Review incoming passenger requests and accept/decline. |
| **Calculate Fuel Cost Share** | System | Compute proportional cost share split per passenger. |
| **View / Manage Bookings** | Rider Commuter, Driver Host | Track active, upcoming, and completed ride bookings. |
| **Rate Ride / User** | Rider Commuter, Driver Host | Submit rating and performance feedback post-trip. |

---

### 3. UML Relationship Specification

#### `<<include>>` Relationships (Mandatory Sub-processes)
1. **`Create Driver Profile` $\xrightarrow{<<include>>}$ `Verify Driver / Vehicle`**
   * *Rationale:* Submitting and verifying official identity and vehicle documents is mandatory when creating a Driver Host profile before posting ride offers.
2. **`Search for Carpool Matches` $\xrightarrow{<<include>>}$ `Calculate Route Compatibility`**
   * *Rationale:* Querying for matches automatically executes the route compatibility algorithm to enforce the 1.5 km detour tolerance limit.
3. **`Request a Ride` $\xrightarrow{<<include>>}$ `Calculate Fuel Cost Share`**
   * *Rationale:* Requesting a ride automatically calculates the estimated fuel cost split for transparency.

#### `<<extend>>` Relationships (Optional / Conditional Extensions)
1. **`Rate Ride / User` $\xrightarrow{<<extend>>}$ `View / Manage Bookings`**
   * *Rationale:* Rating a ride extends booking management conditionally upon successful trip completion.
