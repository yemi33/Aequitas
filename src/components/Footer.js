import React from "react";

export default function Footer({style="fixed"}) {
  return (
    <div className="footer" style={{"position": style}}>
      © Carleton College Aequitas
    </div>
  );
}
