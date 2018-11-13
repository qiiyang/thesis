import colours.paletton_bauhaus_itten as bauhaus
from colours import gray
#from colormath.color_objects import sRGBColor, LabColor
#from colormath.color_conversions import convert_color

# Primary, complementary, 2 adjacent
c0 = bauhaus.blue # Blue
c1 = bauhaus.violet # Violet
c2 = bauhaus.green # Green
c3 = bauhaus.orange #Orange

# Sample designation
s1 = c1[2]
s2 = c0[2]
s3 = c3[3]
s4 = c2[4]
bl1 = "#e61717"
bl2 = "#e67517"
bl3 = "#12b812"
bl4 = "#6b1799"


# Temperature Scale
t2 = c1[4]
t4 = c0[3]
t8 = c0[1]
t12 = c2[1]
t16 = c3[1]
t30 = c3[3]

# general
aid_lines = gray.c4

# colours for XRD
xrd_eus = gray.c4
xrd1 = s1
xrd2 = s2
xrd3 = s3
xrd4 = s4
xrd_peak_label = gray.c5

# colours for squid
squid_T = c0[2]
squid_Ha = c0[2]
squid_Hb = c1[0]

# colours for MI
mi_re = c0[2]  # real
mi_im = c3[3]  # imaginary

# Colours for RvT
rvt1 = s1
rvt2 = s2
rvt3 = s3
rvt4 = s4

# Colours for Hall
hall1 = s1
hall2 = s2
hall3 = s3
hall4 = s4

# Colours for WL_trend
wl_yes = c1[1]
wl_no = gray.c3
wl_maybe = c0[2]


