import streamlit as st

from streamlit_editorjs import st_editorjs

st.set_page_config(page_title="Editor.js", layout="wide")

initial_doc = {
  "time": 1760000000000,
  "blocks": [
    {
      "id": "title",
      "type": "header",
      "data": {
        "text": "Ihr unverzichtbarer Leitfaden zur ITB26 in Berlin",
        "level": 1
      }
    },
    {
      "id": "excerpt",
      "type": "paragraph",
      "data": {
        "text": "Bereiten Sie sich auf die ITB26 vor, ein bedeutendes Event, das auf der Messe Berlin stattfindet. Dieses Treffen vereint verschiedene Aspekte der Reisewelt und bietet eine einzigartige Gelegenheit, die pulsierende Stadt Berlin zu erkunden."
      }
    },
    {
      "id": "section-1-heading",
      "type": "header",
      "data": {
        "text": "Über die ITB26",
        "level": 2
      }
    },
    {
      "id": "section-1-body",
      "type": "paragraph",
      "data": {
        "text": "Die ITB26 ist eine renommierte Veranstaltung, die sich auf die globale Reisebranche konzentriert. Auf der weitläufigen Messe Berlin abgehalten, dient sie als wichtiger Treffpunkt für Fachleute und Enthusiasten gleichermaßen. Während die spezifischen Details des Programms jedes Jahr variieren, bietet die Veranstaltung stets Einblicke in aufkommende Trends und Reiseziele. Gäste, die die ITB26 besuchen, finden sich im Zentrum von Diskussionen wieder, die zukünftige Reiseerlebnisse prägen. Es ist eine ausgezeichnete Gelegenheit, sich mit der weiteren Welt des Tourismus zu vernetzen."
      }
    },
    {
      "id": "section-2-heading",
      "type": "header",
      "data": {
        "text": "Erstklassige Lage auf der Messe Berlin",
        "level": 2
      }
    },
    {
      "id": "section-2-body",
      "type": "paragraph",
      "data": {
        "text": "Die Messe Berlin bietet einen idealen Rahmen für eine Veranstaltung dieser Größenordnung. Günstig in Berlin, Deutschland, gelegen, bieten die Messegelände hervorragende Anbindungen an die öffentlichen Verkehrsmittel, was einen einfachen Zugang für alle Teilnehmer gewährleistet. Ein Aufenthalt in der Nähe der Messe Berlin bedeutet weniger Reisezeit und mehr Gelegenheit, sich mit der Veranstaltung zu beschäftigen. Diese zentrale Lage bringt Sie auch in Reichweite von Berlins vielfältigen Attraktionen und verbindet Geschäftliches nahtlos mit Freizeit für einen lohnenden Besuch."
      }
    },
    {
      "id": "section-3-heading",
      "type": "header",
      "data": {
        "text": "Berlins Reize entdecken",
        "level": 2
      }
    },
    {
      "id": "section-3-body",
      "type": "paragraph",
      "data": {
        "text": "Jenseits der Veranstaltung lädt Berlin Sie ein, seine reiche Geschichte und zeitgenössische Kultur zu erkunden. Von ikonischen Wahrzeichen bis hin zu belebten Vierteln bietet die Stadt eine fesselnde Atmosphäre für jeden Gast. Genießen Sie erstklassige Restaurants, innovative Kunstszenen und ruhige Grünflächen. Sich Zeit zu nehmen, Berlin zu entdecken, bereichert Ihr Gesamterlebnis und verwandelt einen Veranstaltungsbesuch in einen unvergesslichen deutschen Kurzurlaub. Unser Ziel ist es, sicherzustellen, dass Ihr Aufenthalt sowohl produktiv als auch zutiefst angenehm ist."
      }
    },
    {
      "id": "section-4-heading",
      "type": "header",
      "data": {
        "text": "Nahtloses Reiseerlebnis",
        "level": 2
      }
    },
    {
      "id": "section-4-body",
      "type": "paragraph",
      "data": {
        "text": "Für diejenigen, die die ITB26 besuchen, ist ein reibungsloser und komfortabler Aufenthalt von größter Bedeutung. Unsere Unterkünfte sollen nach einem anstrengenden Tag auf der Messe Berlin einen einladenden Rückzugsort bieten. Wir konzentrieren uns darauf, Bequemlichkeit zu bieten, von einfachen Buchungsprozessen bis hin zu hilfreichen lokalen Empfehlungen. Die Gewährleistung Ihres Komforts ermöglicht es Ihnen, sich voll und ganz in die Veranstaltung und die Stadt einzutauchen, ohne zusätzlichen Stress. Lassen Sie uns Ihren Besuch in Berlin bereichern und ihn wirklich außergewöhnlich machen."
      }
    }
  ],
  "version": "2.30.0"
}

st.session_state.setdefault("doc", initial_doc)

edited_doc = st_editorjs(
    value=st.session_state.doc,
    key="main_editor",
    height=500,
    placeholder="Start writing...",
    debounce_ms=400,
)

if edited_doc != st.session_state.doc:
    st.session_state.doc = edited_doc

if st.button("Reset"):
    st.session_state.doc = initial_doc
    st.rerun()
