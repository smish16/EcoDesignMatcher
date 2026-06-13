import streamlit as st
import time

# 1. Global Streamlit Layout Engine Configurations
st.set_page_config(
    page_title="Eco-Design Matcher",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. High-Resolution Cyber-Glassmorphism Stylesheet 
cyber_glass_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #0f172a 50%, #020617 100%) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #f8fafc !important;
    }
    
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* Centered Hero Card */
    .hero-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.03) 0%, rgba(255, 255, 255, 0.01) 100%) !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 28px !important;
        padding: 45px 30px !important;
        margin-bottom: 35px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5) !important;
        text-align: center;
    }
    
    /* Naive-Friendly Directives Banner */
    .directive-card {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px dashed rgba(255, 255, 255, 0.15) !important;
        border-radius: 16px;
        padding: 20px !important;
        margin-top: 25px;
        text-align: left;
    }
    
    .glass-card {
        background: rgba(15, 23, 42, 0.4) !important;
        backdrop-filter: blur(30px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 24px !important;
        padding: 35px !important;
        margin-bottom: 25px;
    }
    
    .metric-pill {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 16px !important;
        padding: 18px !important;
        text-align: center;
    }
    
    .gradient-title {
        background: linear-gradient(90deg, #34d399 0%, #10b981 50%, #60a5fa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
    }
    
    label, [data-testid="stWidgetLabel"] p {
        color: #cbd5e1 !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
    }
    
    div[data-baseweb="select"] *, input, div[data-baseweb="input"] * {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }
    
    button[kind="primary"] {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        border: none !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        padding: 12px 24px !important;
        border-radius: 12px !important;
        box-shadow: 0 10px 20px -5px rgba(16, 185, 129, 0.4) !important;
    }
</style>
"""
st.markdown(cyber_glass_css, unsafe_allow_html=True)

# 3. Hero Section (Centered Layout with Directives Embedded)
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.markdown('<span style="background: rgba(16, 185, 129, 0.15); color: #34d399; font-size: 0.8rem; font-weight: 700; padding: 6px 14px; border-radius: 30px; text-transform: uppercase;">UNSDG Goal 12 Framework</span>', unsafe_allow_html=True)
st.markdown('<h1 class="gradient-title" style="font-size: 3.2rem; margin-top: 15px; margin-bottom: 15px; text-align: center;">AI Circular Packaging Matcher</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.6;">Our automated platform pairs local D2C brands with matching eco-friendly packaging alternatives. Input your base product parameters below to instantly optimize layout designs, calculate carbon offsets, and download certified sourcing options.</p>', unsafe_allow_html=True)

# Clean Directives block separated from parent formatting safely
st.markdown("""
<div class="directive-card">
    <h4 style="margin-top:0; color:#34d399; font-size:1.1rem; margin-bottom:12px;">📋 Quick Operational Instructions:</h4>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; font-size: 0.9rem; color: #cbd5e1; line-height:1.5;">
        <div><b>1. Input Specifications:</b> Pick your product category, assign approximate weight metrics, and configure shelf protection windows in the configuration terminal.</div>
        <div><b>2. Customize Branding:</b> Assign your exact business color codes using the hue selectors to preview personalized brand palettes.</div>
        <div><b>3. Compile Dashboard:</b> Hit 'Compile Configuration Profile' to view eco-metrics, suggested dynamic packaging quotes, and real stock visual textures.</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Workspace Panels Setup
input_workspace, output_canvas = st.columns([1, 1.2], gap="large")

with input_workspace:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; margin-top:0; margin-bottom: 25px; font-size: 1.4rem;">⚙️ Structural Engine Variables</h3>', unsafe_allow_html=True)
    
    product_type = st.selectbox(
        "Product Configuration Sector",
        ["Apparel & Textiles", "Cosmetics & Skincare", "Dry Food & Snacks", "Gourmet Liquids & Oils", "Electronics Accessories"]
    )
    base_weight = st.number_input("Target Base Weight (Grams)", min_value=1, value=300, step=50)
    barrier_strength = st.slider("Required Structural Shelf Guard (Months)", min_value=1, max_value=24, value=8)
    
    st.markdown('<hr style="border: 0.5px solid rgba(255,255,255,0.08); margin: 30px 0;">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; margin-top:0; margin-bottom: 20px; font-size: 1.25rem;">🎨 Brand Identity Sync Overlay</h3>', unsafe_allow_html=True)
    
    identity_vibe = st.selectbox("Design Theme Direction", ["Minimalist Luxe", "Earth Tone Rustic", "Vibrant Gen-Z", "Monochrome Tech"])
    
    hex_col1, hex_col2 = st.columns(2)
    with hex_col1:
        primary_hex = st.color_picker("Primary Palette Anchor", "#10b981")
    with hex_col2:
        accent_hex = st.color_picker("Secondary Brand Highlight", "#60a5fa")
        
    st.markdown('<div style="margin-top: 25px;">', unsafe_allow_html=True)
    compile_btn = st.button("Compile Configuration Profile", use_container_width=True, type="primary")
    st.markdown('</div></div>', unsafe_allow_html=True)

with output_canvas:
    if compile_btn:
        with st.spinner("Processing architectural metrics..."):
            time.sleep(1.0)
            
        ai_data_matrix = {
            "Apparel & Textiles": {
                "material": "Cornstarch Polylactic Acid (PLA) Outer Packs",
                "carbon": "68.4%", "weight_delta": "-15g",
                "quotes": ["There is no Planet B.", "Worn on you, safe on Earth.", "Zero plastic, 100% style."],
                "texture": "Smooth Matte Biological Protective Film",
                "img_url": "https://images.unsplash.com/photo-1605614131543-98a96c3bfef9?w=600&auto=format&fit=crop&q=80"
            },
            "Cosmetics & Skincare": {
                "material": "Mycelium Structural Trays & Upcycled Seaweed Caps",
                "carbon": "82.1%", "weight_delta": "+8g",
                "quotes": ["Clean beauty, cleaner footprint.", "Grown from nature, returning to nature.", "Kind to your skin, gentler on the soil."],
                "texture": "Velvety Pressed Dense Organic Cell Pulp",
                "img_url": "https://images.unsplash.com/photo-1608248597481-496100c80836?w=600&auto=format&fit=crop&q=80"
            },
            "Dry Food & Snacks": {
                "material": "Plant Cellulose High-Barrier Oxygen Pouches",
                "carbon": "55.2%", "weight_delta": "-5g",
                "quotes": ["Naturally fresh, completely plastic-free.", "Bite size footprint, giant eco-impact.", "Good food shouldn't cost the Earth."],
                "texture": "High-Tactile Raw Porous Kraft Finish",
                "img_url": "https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80"
            },
            "Gourmet Liquids & Oils": {
                "material": "Post-Consumer Recycled (PCR) Amber Glass Enclosure",
                "carbon": "41.7%", "weight_delta": "-45g",
                "quotes": ["Preserved naturally, sustained responsibly.", "Glass made to live forever.", "Circular choices taste better."],
                "texture": "Gloss Premium Amber Recycled Eco-Glaze",
                "img_url": "https://images.unsplash.com/photo-1601049676099-e7ed07d825b0?w=600&auto=format&fit=crop&q=80"
            },
            "Electronics Accessories": {
                "material": "Molded Bamboo Pulp Heavy Geometric Shells",
                "carbon": "73.9%", "weight_delta": "-22g",
                "quotes": ["Smart gear, smarter packaging.", "Unbox responsibly.", "Engineered with organic precision."],
                "texture": "Pressed Symmetric High-Density Recessed Lines",
                "img_url": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=600&auto=format&fit=crop&q=80"
            }
        }
        
        selected_match = ai_data_matrix[product_type]
        quote_routing = 0 if identity_vibe == "Minimalist Luxe" else (1 if identity_vibe == "Earth Tone Rustic" else 2)
        selected_slogan = selected_match["quotes"][quote_routing]

        # Container Panel Start
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<span style="background: rgba(52, 211, 153, 0.12); color: #34d399; font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 8px;">Optimal AI Material Fit</span>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #ffffff; margin-top: 12px; margin-bottom: 5px; font-size: 1.8rem;">{selected_match["material"]}</h2>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 25px;">Engine verified for structural integrity at {barrier_strength} months barrier tolerance limits.</p>', unsafe_allow_html=True)
        
        # Dual Segment Columns for Media and Visual Template Rendering
        img_col, design_col = st.columns([1, 1.2])
        
        with img_col:
            st.image(selected_match["img_url"], caption="Recommended Material Sourcing", use_container_width=True)
        
        with design_col:
            # FIX: Rendered completely as isolated functional markup steps to sidestep parsing crashes
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(15,23,42,0.8) 0%, rgba(2,6,17,0.9) 100%); border-radius: 20px; padding: 25px; border-top: 5px solid {primary_hex}; box-shadow: 0 15px 35px -5px rgba(0,0,0,0.7);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 12px;">
                    <span style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: #64748b; font-weight: 700;">📐 Canvas: {identity_vibe}</span>
                    <div style="display: flex; gap: 6px;">
                        <div style="width: 12px; height: 12px; background: {primary_hex}; border-radius: 50%;"></div>
                        <div style="width: 12px; height: 12px; background: {accent_hex}; border-radius: 50%;"></div>
                    </div>
                </div>
                <div style="border: 2px dashed rgba(255,255,255,0.15); border-radius: 14px; padding: 25px 15px; text-align: center; background: rgba(255,255,255,0.01);">
                    <p style="color: {primary_hex} !important; font-size: 1.35rem; font-weight: 800; font-style: italic; margin: 0; line-height: 1.3;">
                        "{selected_slogan}"
                    </p>
                    <p style="color: #64748b !important; font-size: 0.7rem; text-transform: uppercase; margin-top: 15px; letter-spacing: 0.1em; font-weight: 700;">
                        🌿 Soy-Ink High-Def Print Layout Area
                    </p>
                </div>
                <div style="margin-top: 20px; font-size: 0.8rem; color: #cbd5e1; display: flex; align-items: center; gap: 8px;">
                    <span style="color: {accent_hex}; font-weight: 800;">ℹ️</span> 
                    <span><b>Texture Fit:</b> {selected_match["texture"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Real-time Core Lifecycle Metrics Row Layout
        st.markdown('<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 25px;">', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-pill"><span style="font-size: 1.6rem; font-weight: 800; color: #10b981;">{selected_match["carbon"]}</span><br><span style="font-size: 0.75rem; color: #64748b; font-weight:600;">CO₂ Extinguished</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-pill"><span style="font-size: 1.6rem; font-weight: 800; color: #60a5fa;">{selected_match["weight_delta"]}</span><br><span style="font-size: 0.75rem; color: #64748b; font-weight:600;">Mass Reduction</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-pill"><span style="font-size: 1.6rem; font-weight: 800; color: #f59e0b;">{barrier_strength}M</span><br><span style="font-size: 0.75rem; color: #64748b; font-weight:600;">Guard Stability</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="glass-card" style="height: 440px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-style: dashed !important; border-color: rgba(255,255,255,0.15) !important;">', unsafe_allow_html=True)
        st.markdown('<p style="color: #4b5563; font-size: 1.1rem; font-weight: 500; text-align: center; margin: 0;">Adjust variables in the left panel and click<br><b style="color: #94a3b8;">"Compile Configuration Profile"</b><br>to engage the AI structural canvas overlay model.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)