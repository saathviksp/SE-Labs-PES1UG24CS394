# Use-Case Flow Specification: Request a Ride

## Use Case Information
- **Use Case ID:** UC-009
- **Use Case Name:** Request a Ride
- **Primary Actor:** Rider Commuter
- **Supporting Actor:** Driver Host
- **Goal:** To enable a Rider Commuter to search for overlapping commute routes, verify 1.5 km detour compatibility, view estimated fuel cost share breakdowns, and submit a seat booking request to a Driver Host for approval.

---

## Preconditions
1. Both Rider Commuter and Driver Host are registered, authenticated, and logged into the system.
2. The Driver Host has a verified profile with valid driving credentials and a published daily commute route with available seats.
3. The Rider Commuter has set an active commute origin, destination, and departure time window.

---

## Postconditions
1. The ride booking status is updated to **"Confirmed"** in the system repository.
2. The available seat count for the Driver Host's scheduled trip is decremented by one.
3. An **estimated** fuel cost share split is computed and attached to the pending booking request (with final itemized settlement calculated upon ride completion per `FR-002`).
4. Real-time booking confirmations and itinerary notifications are dispatched to both the Rider Commuter and Driver Host.

---

## Main Success Scenario
1. **Search Carpool Rides:** The Rider Commuter initiates a search for carpool matches by providing their daily pickup/dropoff locations and departure time window.
2. **Calculate Route Compatibility (`<<include>>` UC-007):** The system automatically evaluates candidate Driver Host routes against the Rider Commuter's path to determine if the added detour distance is within the mandatory **1.5 km detour tolerance threshold** (`FR-001`).
3. **Calculate Estimated Fuel Cost Share (`<<include>>` UC-011):** For compatible routes, the system calculates the **estimated** fuel cost share split based on trip distance, vehicle fuel efficiency, and current fuel rates (`FR-002`). *Note: The final itemized cost split bill is generated upon completion of the shared ride.*
4. **Display Matches:** The system displays a sorted list of compatible carpool matches showing driver ratings, estimated pickup time, added detour distance, and estimated fuel cost share.
5. **Submit Request:** The Rider Commuter selects a preferred Driver Host route and submits a seat request.
6. **Set Pending State:** The system places the seat in a temporary hold state ("Pending Approval") and sends an instant booking notification to the Driver Host (`FR-005`).
7. **Driver Approval:** The Driver Host reviews the passenger profile, pickup point, and detour metric, and accepts the ride request within the 30-minute response window.
8. **Confirm Booking:** The system updates the booking status to **"Confirmed"**, updates vehicle seat availability, and sends final itinerary details to both actors.

---

## Alternate Flows

### Alternate Flow 3a: Detour Tolerance Exceeded
* **Trigger:** The calculated added detour distance for a candidate Driver Host route exceeds **1.5 km**.
* **Flow:**
  1. The system flags the route as incompatible under requirement `FR-001`.
  2. The system excludes the route from the search results.
  3. If no routes fall within 1.5 km, the system displays: *"No compatible carpool matches found within your 1.5 km detour preference."*
  4. The Rider Commuter is prompted to adjust their departure time window or pickup location.

### Alternate Flow 7a: Driver Host Rejects Request or Request Expires
* **Trigger:** The Driver Host manually declines the request or fails to respond within the 30-minute window.
* **Flow:**
  1. The system updates the booking status to **"Declined"** or **"Expired"**.
  2. The temporary seat hold is released back to the Driver Host's available capacity.
  3. The system sends a notification to the Rider Commuter informing them of the refusal.
  4. The system prompts the Rider Commuter to select another match from their search results list.
