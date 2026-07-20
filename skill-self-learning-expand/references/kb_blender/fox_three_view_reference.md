**Red Fox 3D Modeling Reference Sheet (Blender Units)**  
*Body length = 1.6 units*

---

## **THREE-VIEW PROPORTIONS**

### **FRONT VIEW (XZ plane, looking from Y+)**
- **Total width at widest point (shoulders):** 0.85
- **Width at hips:** 0.70
- **Chest width:** 0.50
- **Neck width at base:** 0.25
- **Neck width at head:** 0.20
- **Head width (across cheeks):** 0.35
- **Head width at snout:** 0.12
- **Ear width at base:** 0.12
- **Ear height above head:** 0.30
- **Ear tip:** pointed, angle outward ~15°
- **Distance between inner ear bases:** 0.20
- **Eye position:** 0.28 from top of head, 0.12 from centerline
- **Eye size:** 0.05 radius
- **Nose position:** center, at snout tip
- **Nose size:** 0.04 radius
- **Leg width:** 0.06 radius
- **Front legs:** shoulder width apart (0.50 between outer edges)
- **Back legs:** hip width apart (0.45 between outer edges)
- **Paw width:** 0.08

---

### **SIDE VIEW (YZ plane, looking from X+)**
- **Total length (nose to tail base):** 1.60
- **Total height (ground to ear tip):** 1.10
- **Body height (ground to top of back):** 0.35
- **Body length (chest to rump):** 1.10
- **Neck length (base to head):** 0.25
- **Head length (back to nose):** 0.50
- **Snout length:** 0.20
- **Snout angle:** slightly downward (5°)
- **Eye position from snout tip:** 0.15 back
- **Ear position:** above eyes, 0.30 from back of head
- **Front leg height:** 0.65
- **Front leg position from nose:** 0.50
- **Back leg height:** 0.50
- **Back leg position from nose:** 1.10
- **Tail attachment:** at rump, 0.10 above ground
- **Tail length:** 1.50
- **Tail thickness at base:** 0.10
- **Tail thickness at mid:** 0.16
- **Tail thickness at tip:** 0.04
- **Tail curve:** starts at 45° down, curves in S-shape

---

### **BACK VIEW (XZ plane, looking from Y-)**
- **Same as front view for symmetry**
- **Ear tips visible from behind**
- **Neck visible between shoulders**
- **Tail centered on spine**

---

## **COLOR PATTERN (HEX codes)**

| Part              | Color       |
|-------------------|-------------|
| Body main         | #D4693D     |
| Belly/chest       | #F5F0E1     |
| Muzzle/chin       | #F5F0E1     |
| Ear tips/edges    | #2A2A2A     |
| Paw lower half    | #2A2A2A     |
| Tail tip (last 25%) | #F5F0E1   |
| Eye               | #1A1A1A     |

---

## **BLENDER MODELING INSTRUCTIONS**

1. **Use Mirror modifier on X axis** for all symmetrical parts.
2. **Apply Subdivision Surface modifier** on all organic parts (body, head, ears, tail).
3. **Modeling order:**
   - **Body**
   - **Head**
   - **Ears**
   - **Legs**
   - **Tail**
4. **Body:**
   - Start with a subdivided cube.
   - Shape into an elliptical form.
   - Use proportional editing and edge loops for smooth transitions.
5. **Head:**
   - Extrude from the neck area.
   - Shape with careful attention to cheekbones and snout.
6. **Ears:**
   - Triangular extrusions from the top of the head.
   - Tip angled outward by ~15°.
7. **Legs:**
   - Cylinders with slight taper.
   - Front legs placed 0.50 apart (outer edges), back legs 0.45 apart.
8. **Tail:**
   - Cone shape with Subdivision Surface.
   - Use Simple Deform modifier (Bend) to create S-shaped curve.
   - Adjust thickness along the tail: 0.10 (base), 0.16 (mid), 0.04 (tip).

---

## **SILHOUETTE CHECKLIST**

- [ ] **Front:** Narrow pointy ears, V-shaped face, wider at cheeks, narrower at neck  
- [ ] **Side:** Arched back (higher at shoulders), sloped rump, head pointing slightly down  
- [ ] **Back:** Ears visible above shoulders, tail centered  
- [ ] **Total height:width ratio:** ~1.3:1 (front view)  
- [ ] **Total length:height ratio:** ~1.75:1 (side view)

---

## **EXACT BLENDER UNIT VALUES FOR USE IN SCRIPTS OR MODIFIERS**

### **Front View Dimensions (XZ Plane):**
- Shoulder width: 0.85
- Hip width: 0.70
- Chest width: 0.50
- Neck base width: 0.25
- Neck head width: 0.20
- Head width (cheeks): 0.35
- Head snout width: 0.12
- Ear base width: 0.12
- Ear height: 0.30
- Ear tip angle: 15° outward
- Ear spacing (inner base): 0.20
- Eye Y-position: 0.28 (from top of head)
- Eye X-position: 0.12 (from centerline)
- Eye radius: 0.05
- Nose radius: 0.04
- Leg radius: 0.06
- Front leg spacing: 0.50 (outer edges)
- Back leg spacing: 0.45 (outer edges)
- Paw width: 0.08

### **Side View Dimensions (YZ Plane):**
- Total length: 1.60
- Total height: 1.10
- Body height: 0.35
- Body length: 1.10
- Neck length: 0.25
- Head length: 0.50
- Snout length: 0.20
- Snout angle: 5° downward
- Eye position from snout: 0.15
- Ear position from back of head: 0.30
- Front leg height: 0.65
- Front leg position from nose: 0.50
- Back leg height: 0.50
- Back leg position from nose: 1.10
- Tail attachment height: 0.10
- Tail length: 1.50
- Tail base thickness: 0.10
- Tail mid thickness: 0.16
- Tail tip thickness: 0.04
- Tail curve: 45° downward start, S-shaped curve

---

This reference sheet is designed for precision modeling in Blender, ensuring accurate proportions and visual fidelity for a red fox character.