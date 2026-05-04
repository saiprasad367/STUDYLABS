import os

BASE = r"c:\Users\saipr\Videos\studylabs\public_html"

def write_file(name, content):
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {name}")

NAV = """<ul id="nav" class="nav main-menu menu navbar-nav">
<li><a href="index.html"><i class="fa fa-home"></i></a></li>
<li class="icon-active"><a href="#">Products</a><ul class="sub-menu"><li><a href="bandage.html">Medical Bandage</a></li><li><a href="smart-watch.html">Smart Watch</a></li><li><a href="silicone-belt.html">Silicone Belt</a></li><li><a href="silicone-gaskets.html">Silicone Gaskets</a></li><li><a href="silicone-ring.html">Silicone Ring</a></li></ul></li>
<li class="icon-active"><a href="#">Testing Services</a><ul class="sub-menu">
  <li class="icon-active"><a href="processing-equipments.html">Processing Equipments</a><ul class="sub-menu">
    <li><a href="processing-equipments.html">Environmental Controlled High Temperature Furnace</a></li>
    <li><a href="processing-equipments.html">Specimen Cutting Machine</a></li>
    <li><a href="processing-equipments.html">Single/Double Disc Polishing Machine</a></li>
    <li><a href="processing-equipments.html">Universal Testing Machine</a></li>
  </ul></li>
  <li class="icon-active"><a href="characterization-equipments.html">Characterization Equipment</a><ul class="sub-menu">
    <li><a href="characterization-equipments.html">Shore A Durometer</a></li>
    <li><a href="characterization-equipments.html">Shore D Durometer</a></li>
    <li><a href="characterization-equipments.html">Metallography Station Trinolcular Optical Microscope</a></li>
    <li><a href="characterization-equipments.html">Surface Roughness Tester</a></li>
    <li><a href="characterization-equipments.html">Superficial Rockwell Tester</a></li>
    <li><a href="characterization-equipments.html">Brinell Hardness Tester</a></li>
    <li><a href="characterization-equipments.html">Vickers Hardness Tester</a></li>
  </ul></li>
</ul></li>
<li><a href="education.html">Professional Education</a></li>
<li class="icon-active"><a href="#">Research</a><ul class="sub-menu">
  <li><a href="materials.html">Materials</a></li>
  <li><a href="technology.html">Manufacturing Technology</a></li>
  <li><a href="energy.html">Energy</a></li>
</ul></li>
<li><a href="portfolio.html">Gallery</a></li>
<li><a href="about.html">About</a></li>
<li><a href="certifications.html">Certifications</a></li>
<li><a href="projects.html">Projects</a></li>
<li class="mobile-only-nav"><a href="ip.html">IP Details</a></li>
<li class="mobile-only-nav"><a href="contact.html">Contact Us</a></li>
</ul>"""

def TOPBAR():
    return f"""<header class="header style2">
<div class="topbar"><div class="container"><div class="row">
<div class="col-lg-3 col-12"><div class="logo"><div class="img-logo"><a href="index.html"><img src="images/logo.png" alt="Logo"></a></div></div><div class="mobile-nav"></div></div>
<div class="col-lg-9 col-12 d-flex align-items-center justify-content-end"><div class="topbar-right"><div class="top-contact"><div class="single-contact"><i class="fa fa-copyright"></i><a href="ip.html">IP Details</a></div><a href="contact.html" class="bizwheel-btn theme-2">Contact Us</a></div></div></div>
</div></div></div>
<div class="middle-header"><div class="container"><div class="row"><div class="col-12"><div class="middle-inner"><div class="row"><div class="col-lg-12 col-md-9 col-12"><div class="menu-area"><nav class="navbar navbar-expand-lg"><div class="navbar-collapse"><div class="nav-inner"><div class="menu-home-menu-container">
{NAV}
</div></div></div></nav></div></div></div></div></div></div></div>
</header>"""

FOOTER = """<footer class="footer"><div class="footer-top"><div class="container"><div class="row">
<div class="col-lg-5 col-md-6 col-12"><div class="single-widget footer-about widget"><div class="logo"><div class="img-logo"><a href="index.html"><img class="img-responsive w-75" src="images/logo-white.png" alt="logo"></a></div></div><div class="footer-widget-about-description"><p>Materials Testing is a range of highly precise and reliable techniques that determine</p></div><div class="social"><ul class="social-icons"><li><a href="#" target="_blank"><i class="fa fa-facebook"></i></a></li><li><a href="#" target="_blank"><i class="fa fa-twitter"></i></a></li><li><a href="#" target="_blank"><i class="fa fa-linkedin"></i></a></li><li><a href="https://www.youtube.com/channel/UClhsgA5PVI4BKf4uVENhqEQ" target="_blank"><i class="fa fa-youtube"></i></a></li><li><a href="#" target="_blank"><i class="fa fa-instagram"></i></a></li></ul></div><div class="button"><a href="about.html" class="bizwheel-btn">About Us</a></div></div></div>
<div class="col-lg-3 col-md-6 col-12"><div class="single-widget f-link widget"><h3 class="widget-title">Company</h3><ul><li><a href="processing-equipments.html">Testing Services</a></li><li><a href="education.html">Professional Education</a></li><li><a href="materials.html">Research</a></li><li><a href="portfolio.html">Gallery</a></li><li><a href="about.html">About</a></li><li><a href="certifications.html">Certifications</a></li><li><a href="projects.html">Projects</a></li></ul></div></div>
<div class="col-lg-4 col-md-6 col-12"><div class="single-widget footer_contact widget"><h3 class="widget-title">Contact</h3><p>We always ready to help you. Feel free to contact us</p><ul class="address-widget-list"><li class="footer-mobile-number"><i class="fa fa-phone"></i>+(91) 8688825319</li><li class="footer-mobile-number"><i class="fa fa-envelope"></i>director@studylitcslabs.com</li><li class="footer-mobile-number"><i class="fa fa-map-marker"></i>HNo: 35-3-1472, Kanakadurga colony, Road no 3, Gopalpur, Hanmakonda, Warangal urban, Telangana. India - 506009</li></ul></div></div>
</div></div></div><div class="copyright"><div class="container"><div class="row"><div class="col-12"><div class="copyright-content"><p>© Copyright Studylyticslabs.com</p></div></div></div></div></div></footer>"""

SCRIPTS = """<script src="js/jquery.min.js"></script>
<script src="js/jquery-migrate-3.0.0.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/owl-carousel.min.js"></script>
<script src="js/slicknav.min.js"></script>
<script src="js/easing.js"></script>
<script src="js/scrollup.js"></script>
<script src="js/magnific-popup.min.js"></script>
<script src="js/premium.js"></script>
</body></html>"""

def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>{title} — Studylitcs Labs</title>
<link rel="icon" type="image/png" href="images/favicon.png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/bootstrap.min.css">
<link rel="stylesheet" href="css/font-awesome.css">
<link rel="stylesheet" href="css/slicknav.min.css">
<link rel="stylesheet" href="css/owl-carousel.min.css">
<link rel="stylesheet" href="css/magnific-popup.min.css">
<link rel="stylesheet" href="css/premium.css">
</head>
<body>
<!-- Custom Cursor -->
<div id="cursor-dot"></div>
<div id="cursor-ring"></div>

<!-- Page Transition -->
<div class="page-transition"></div>
<div id="page" class="site">
<div class="preeloader"><div class="preloader-spinner"></div></div>"""

def bc(name, file):
    return f"""<div class="breadcrumbs overlay"><div class="container"><div class="row"><div class="col-12"><div class="bread-inner">
<div class="bread-menu"><ul><li><a href="index.html"><i class="fa fa-home"></i></a></li><li><a href="{file}">{name}</a></li></ul></div>
<div class="bread-title"><h2>{name}</h2></div>
</div></div></div></div></div>"""

def product_gallery(folder, images, captions):
    items = ""
    for img, cap in zip(images, captions):
        items += f"""<div class="col-lg-4 col-md-4 col-sm-6 col-12 reveal" style="margin-bottom:28px;">
<div class="single-team">
<div class="team-head"><img src="images/{folder}/{img}" alt="{cap}" style="height:220px;width:100%;object-fit:cover;"></div>
<div class="t-content"><div class="content-inner"><p class="designation">{cap}</p></div></div>
</div></div>"""
    return f"""<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">
<div class="row">{items}</div>
</div></section>"""

def section_wrap(content):
    return f"""<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">{content}</div></section>"""

def equipment_cards(items_list):
    cards = ""
    for item in items_list:
        cards += f"""<div class="col-lg-6 col-md-6 col-12 reveal" style="margin-bottom:24px;">
<div style="background:var(--bg-white);border:1px solid var(--border);border-radius:var(--radius-lg);padding:28px;box-shadow:var(--shadow-sm);display:flex;align-items:flex-start;gap:16px;transition:var(--transition);">
<div style="width:44px;height:44px;background:var(--accent-light);border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;"><i class="fa fa-cog" style="color:var(--accent);font-size:18px;"></i></div>
<div><h4 style="font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:6px;">{item}</h4></div>
</div></div>"""
    return f'<div class="row">{cards}</div>'

def research_page(title, file, img, intro, list_items, extra=""):
    items_html = "".join([f'<li style="margin-bottom:12px;font-size:15px;color:var(--text-secondary);line-height:1.7;">{i}</li>' for i in list_items])
    extra_html = f'<div class="col-lg-12 col-md-12 col-12 mt-4 reveal"><p style="font-size:15px;color:var(--text-secondary);">{extra}</p></div>' if extra else ""
    return head(title) + TOPBAR() + bc(title, file) + f"""
<section class="about-us"><div class="container"><div class="row">
<div class="col-lg-5 offset-lg-1 col-md-6 col-12 reveal"><div class="modern-img-feature"><img src="{img}" alt="{title}"></div></div>
<div class="col-lg-5 col-md-6 col-12 reveal">
<div class="about-content section-title default text-left">
<div class="section-top"><h1><b>We Provide Quality Business &amp; Smart Solution</b></h1></div>
<div class="section-bottom"><div class="text"><p>{intro}</p></div></div></div>
<ol style="padding-left:24px;margin-top:8px;">{items_html}</ol>
</div>
{extra_html}
</div></div></section>""" + FOOTER + SCRIPTS

# ===================== PORTFOLIO =====================
gallery_items = "".join([
    f'<div class="col-lg-4 col-md-4 col-sm-6 col-12 gallery_product-item reveal" style="padding:8px;"><a href="docs/{i}.jpg" class="image-popup"><img src="docs/{i}.jpg" alt="Lab Image {i}" style="height:220px;width:100%;object-fit:cover;border-radius:12px;box-shadow:var(--shadow-sm);"></a></div>'
    for i in range(1, 19)
])
write_file("portfolio.html", head("Gallery") + TOPBAR() + bc("Gallery","portfolio.html") + f"""
<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">
<div class="section-title text-center reveal" style="margin-bottom:40px;"><div class="section-top"><h1><b>Our Lab Gallery</b></h1></div><div class="section-bottom"><p>A visual walkthrough of our facilities, experiments, and team in action.</p></div></div>
<div class="row">{gallery_items}</div>
</div></section>""" + FOOTER + SCRIPTS)

# ===================== PROJECTS =====================
write_file("projects.html", head("Projects") + TOPBAR() + bc("Projects","projects.html") + """
<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">
<div class="section-title text-center reveal" style="margin-bottom:40px;"><div class="section-top"><h1><b>Our Projects</b></h1></div><div class="section-bottom"><p>Government funded innovation and research projects undertaken by Studylitcs Labs.</p></div></div>
<div class="reveal" style="background:var(--bg-white);border:1px solid var(--border);border-radius:var(--radius-xl);padding:32px;box-shadow:var(--shadow-md);">
<h4 style="font-size:20px;font-weight:700;margin-bottom:20px;color:var(--text-primary);">NIDHI-PRAYAS Project Completion Report <span style="font-size:14px;color:var(--text-muted);font-weight:400;">(06.12.2023)</span></h4>
<iframe src="docs/NIDHI-PRAYAS.pdf" width="100%" height="800px" style="border:none;border-radius:12px;"></iframe>
</div></div></section>""" + FOOTER + SCRIPTS)

# ===================== EDUCATION =====================
write_file("education.html", head("Professional Education") + TOPBAR() + bc("Professional Education","education.html") + """
<section class="about-us"><div class="container"><div class="row">
<div class="col-lg-5 offset-lg-1 col-md-6 col-12 reveal"><div class="modern-img-feature"><img src="images/gallery/img1.jpeg" alt="Education"></div></div>
<div class="col-lg-5 col-md-6 col-12 reveal">
<div class="about-content section-title default text-left">
<div class="section-top"><h1><b>Professional Education</b></h1></div>
<div class="section-bottom"><div class="text">
<p>Studylitcs labs provides extensive professional education in materials testing, characterization, and advanced research techniques in partnership with academic institutions and industry leaders.</p>
<p>Our industry-institute corridor programmes are designed to help aspiring engineers and researchers gain hands-on experience with our state-of-the-art equipment and methods.</p>
</div></div></div>
<ol style="padding-left:24px;margin-top:16px;">
<li style="margin-bottom:10px;font-size:15px;color:var(--text-secondary);">Digital Manufacturing</li>
<li style="margin-bottom:10px;font-size:15px;color:var(--text-secondary);">Additive Manufacturing</li>
<li style="margin-bottom:10px;font-size:15px;color:var(--text-secondary);">Big Data Analytics in Manufacturing</li>
<li style="margin-bottom:10px;font-size:15px;color:var(--text-secondary);">Smart Materials</li>
<li style="margin-bottom:10px;font-size:15px;color:var(--text-secondary);">Renewable Energy Sources</li>
</ol>
</div></div></div></section>""" + FOOTER + SCRIPTS)

# ===================== IP DETAILS =====================
write_file("ip.html", head("IP Details") + TOPBAR() + bc("IP Details","ip.html") + """
<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">
<div class="section-title text-center reveal" style="margin-bottom:40px;"><div class="section-top"><h1><b>Intellectual Property</b></h1></div><div class="section-bottom"><p>Our patents and trademarks reflecting our commitment to innovation.</p></div></div>
<div class="reveal" style="margin-bottom:40px;">
<h3 style="font-size:20px;font-weight:700;margin-bottom:20px;">Patents</h3>
<div style="overflow-x:auto;"><table class="table table-bordered">
<thead><tr><th>S.No</th><th>Title of Invention</th><th>Application Number</th><th>Year</th><th>Status</th></tr></thead>
<tbody>
<tr><td>1</td><td>Polymer wastage in liquid silicone rubber products is reduced by using 3D printed product moulds which can replace the Traditional Injection Moulds Developed for orthopedic medical bandage</td><td>202241056495</td><td>2023</td><td><span style="background:#DCFCE7;color:#16A34A;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;">Granted</span></td></tr>
<tr><td>2</td><td>An Exploratory integration of Geneva with injection molding by means of Automation for reducing the human efforts in the manufacturing of Silicone products</td><td>202241056494</td><td>2023</td><td><span style="background:#DCFCE7;color:#16A34A;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;">Granted</span></td></tr>
<tr><td>3</td><td>Smart watch with speed measuring capabilities</td><td>202241025441 A</td><td>2022</td><td><span style="background:#FEF9C3;color:#B45309;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;">Published</span></td></tr>
<tr><td>4</td><td>Smart watch with solar radiations Trapping Capabilities</td><td>202241004341</td><td>2022</td><td><span style="background:#FEF9C3;color:#B45309;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600;">Published</span></td></tr>
</tbody></table></div></div>
<div class="reveal">
<h3 style="font-size:20px;font-weight:700;margin-bottom:20px;">Trademark</h3>
<div style="overflow-x:auto;"><table class="table table-bordered">
<thead><tr><th>S.No</th><th>Trade Mark</th><th>Temp. Ref No.</th><th>Year</th></tr></thead>
<tbody><tr><td>1</td><td>SHINE INSULATORS</td><td>10528873</td><td>2024</td></tr></tbody>
</table></div></div>
</div></section>""" + FOOTER + SCRIPTS)

# ===================== MEDICAL BANDAGE =====================
write_file("bandage.html", head("Medical Bandage") + TOPBAR() + bc("Medical Bandage","bandage.html") +
product_gallery("medical-bandage",
  ["image01.jpg","image02.jpg","image03.jpg","image04.jpg","image05.jpg","image06.jpg","image07.jpg"],
  ["Liquid silicone rubber mixing with hardner to pour into the Die. Dr.P Sammaiah is guiding the Team Members",
   "Pouring Liquid Silicone Rubber mixture into the Die with the help of injections. Mr Shiv Sai & Mr Aravind are filling the Die with LSR Mixture.",
   "Orthopedic Medical Bandage Prepared with the Liquid silicone rubber",
   "Manohar wore the band on his Elbow to check the flexibility of band.",
   "Mr ShivaSai wore the band on his leg for checking the Sweat, burning, and Muscle pain tests.",
   "Orthopedic medical band wore by Mr ShivSai, and also conducting the some tests on it. Dr.P.Sammaiah, B.Saiprasad is along with him.",
   "Pouring the Liquid Silicone Rubber into the Die."]) + FOOTER + SCRIPTS)

# ===================== SMART WATCH =====================
write_file("smart-watch.html", head("Smart Watch") + TOPBAR() + bc("Smart Watch","smart-watch.html") +
product_gallery("smart-watch",
  ["image01.jpg","image02.jpg","image03.jpg","image04.jpg","image05.jpg","image06.jpg"],
  ["Smart Watch prototype developed at Studylitcs Labs",
   "Aditya Solar Smart Watch - Front view",
   "Smart Watch internals and component assembly",
   "Speed measuring capabilities demonstration",
   "Solar radiation trapping capability test",
   "Smart Watch developed in collaboration with SR Innovation Exchange (SRiX), SR University Warangal"]) + FOOTER + SCRIPTS)

# ===================== SILICONE BELT =====================
write_file("silicone-belt.html", head("Silicone Belt") + TOPBAR() + bc("Silicone Belt","silicone-belt.html") +
product_gallery("",
  ["Silicone-belt.jpg"],
  ["Silicone Belt developed and tested at Studylitcs Labs"]) + FOOTER + SCRIPTS)

# ===================== SILICONE GASKETS =====================
write_file("silicone-gaskets.html", head("Silicone Gaskets") + TOPBAR() + bc("Silicone Gaskets","silicone-gaskets.html") +
product_gallery("silicon-gaskets",
  ["image01.jpg","image02.jpg","image03.jpg","image04.jpg"],
  ["Silicone Gasket — precision engineered",
   "Gasket sealing performance test",
   "Silicone Gasket dimensional inspection",
   "Final quality verified silicone gasket"]) + FOOTER + SCRIPTS)

# ===================== SILICONE RING =====================
write_file("silicone-ring.html", head("Silicone Ring") + TOPBAR() + bc("Silicone Ring","silicone-ring.html") +
product_gallery("silicon-ring",
  ["image01.jpg","image02.jpg","image03.jpg"],
  ["Silicone Ring — moulded with precision",
   "Durability and flexibility testing of silicone ring",
   "Final silicone ring product"]) + FOOTER + SCRIPTS)

# ===================== PROCESSING EQUIPMENTS =====================
proc_equip = ["Environmental Controlled High Temperature Furnace","Specimen Cutting Machine","Single/Double Disc Polishing Machine","Universal Testing Machine"]
write_file("processing-equipments.html", head("Processing Equipments") + TOPBAR() + bc("Processing Equipments","processing-equipments.html") +
f"""<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">
<div class="section-title text-center reveal" style="margin-bottom:40px;"><div class="section-top"><h1><b>Processing Equipments</b></h1></div><div class="section-bottom"><p>State-of-the-art processing equipment available at Studylitcs Labs for materials preparation and forming.</p></div></div>
{equipment_cards(proc_equip)}
<div class="reveal" style="margin-top:40px;">
<div class="modern-img-feature"><img src="images/services/1.png" alt="Processing Equipment" style="width:100%;height:auto;max-height:400px;object-fit:cover;border-radius:var(--radius-xl);"></div>
</div>
</div></section>""" + FOOTER + SCRIPTS)

# ===================== CHARACTERIZATION EQUIPMENTS =====================
char_equip = ["Shore A Durometer","Shore D Durometer","Metallography Station Trinolcular Optical Microscope with Image Analysis Software","Surface Roughness Tester","Superficial Rockwell Tester","Brinell Hardness Tester","Vickers Hardness Tester"]
write_file("characterization-equipments.html", head("Characterization Equipment") + TOPBAR() + bc("Characterization Equipment","characterization-equipments.html") +
f"""<section style="padding:80px 0;background:var(--bg-lighter);">
<div class="container">
<div class="section-title text-center reveal" style="margin-bottom:40px;"><div class="section-top"><h1><b>Characterization Equipment</b></h1></div><div class="section-bottom"><p>Advanced characterization instruments for precise material property evaluation.</p></div></div>
{equipment_cards(char_equip)}
<div class="reveal" style="margin-top:40px;">
<div class="modern-img-feature"><img src="images/services/6.png" alt="Characterization Equipment" style="width:100%;height:auto;max-height:400px;object-fit:cover;border-radius:var(--radius-xl);"></div>
</div>
</div></section>""" + FOOTER + SCRIPTS)

# ===================== MATERIALS =====================
write_file("materials.html", research_page(
  "Materials", "materials.html", "images/gallery/img2.jpeg",
  "We work on different types of materials like composites, ceramics, polymers, and smart materials. Our main focus of latest updates in smart materials are on shape memory alloys, piezoelectric materials, electrostrictive materials, magnetostrictive materials, and smart composites.",
  ["<b>Composite:</b> Currently, composites are used extensively in consumer products and building materials as a light weight, cost efficient alternative to metals. Parts as large as passenger aircraft fuselages are being constructed as a single unit from composite materials.",
   "<b>Ceramics</b> are inorganic, nonmetallic materials (such as carbides, oxides and nitrides) made by shaping at a high temperature. Ceramics are hard, brittle, heat- and corrosion-resistant, and most often have a crystalline structure.",
   "<b>Polymer materials</b> are a kind of important materials that developed rapidly in biological applications. Synthetic polymer materials have many attractive properties, such as monodispersity, biocompatibility, controlled composition and chain length, and tunable chemical properties.",
   "<b>Smart materials</b> have properties that react to changes in their environment. This means that one of their properties can be changed by an external condition, such as temperature, light, pressure, electricity, voltage, pH, or chemical compounds."],
  "Along with this research on types of smart materials we also do our precise work on applications of smart materials like smart materials used in batteries, superconductors, and electronic circuits."))

# ===================== TECHNOLOGY =====================
write_file("technology.html", research_page(
  "Manufacturing Technology", "technology.html", "images/gallery/img2.jpeg",
  "Studylitcs Labs conducts cutting-edge research in manufacturing technology, focusing on innovative production methods, process optimization, and integration of smart manufacturing systems.",
  ["<b>Additive Manufacturing:</b> Research in 3D printing technologies for silicone and composite materials, enabling rapid prototyping and low-waste production.",
   "<b>Injection Moulding Automation:</b> Integration of Geneva mechanisms with injection moulding to reduce human effort and improve product consistency.",
   "<b>3D Printed Moulds:</b> Replacing traditional injection moulds with 3D printed counterparts to reduce polymer wastage and tooling costs.",
   "<b>Process Optimization:</b> Data-driven approaches to optimize cycle times, material utilization, and energy consumption in manufacturing processes.",
   "<b>Smart Manufacturing:</b> Integration of IoT sensors and real-time monitoring systems for predictive maintenance and quality control."]))

# ===================== ENERGY =====================
write_file("energy.html", research_page(
  "Energy Research", "energy.html", "images/gallery/img2.jpeg",
  "Studylitcs Labs actively researches energy harvesting, storage, and conversion technologies, particularly focusing on renewable and smart energy solutions.",
  ["<b>Solar Energy:</b> Research on solar radiation trapping capabilities integrated into wearable devices such as the Aditya Solar Smart Watch.",
   "<b>Smart Materials for Energy:</b> Investigating piezoelectric and magnetostrictive materials for energy harvesting from mechanical vibrations and environmental stimuli.",
   "<b>Superconductors:</b> Exploring smart material applications in superconducting systems for efficient energy transmission.",
   "<b>Battery Technology:</b> Research on smart materials used in next-generation battery cells for improved energy density and longevity.",
   "<b>Renewable Energy Sources:</b> Professional education and research programs focused on solar, wind, and hybrid energy systems for sustainable industrial applications."]))

print("\nAll 15 remaining pages generated successfully!")
