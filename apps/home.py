import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    insert text here____

    """
    )

    m = leafmap.Map(location = [42.569264,20.901489], zoom_start=8)
    m.add_geojson('data/kufiri_ks.geojson')
    m.fit_bounds(m.get_bounds(), padding=(30, 30))
    # m.zoom_to_bounds([[[18.775635,41.619549],[18.775635,43.34116],[23.554688,43.34116],[23.554688,41.619549],[18.775635,41.619549]]])
    # m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
