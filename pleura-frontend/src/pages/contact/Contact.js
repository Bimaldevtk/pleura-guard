import Navbar from "../landing/Navbar";
import "./Contact.css";

function Contact() {
  return (
    <div>
      <Navbar />
      <div className="top-credit">
        <div className="about-title">
          <span>Our</span>Team
        </div>
        <div className="top-content">
          <div>
            <div className="top-name">Prasanth K Baby</div>
            <div>Assistant Professor</div>
            <div>Computer Science Engineering</div>
            <div>Christ College Of Engineering</div>
          </div>
          <div className="side-img-container">
            <img className="sir" src="./Group122.png" alt="photo" />
          </div>
        </div>
      </div>
      <div className="other-container">
        <img src="./contacts.png" alt="photo" />
      </div>
      {/* <div className="software-dev">
        <div className="about-title">
          <span>Our</span>Software Team
        </div>
        <div className="name-container">
          <div>Anagha Sen</div>
          <div>Alan Shibu</div>
          <div>Mohammed Jasrin</div>
          <div>Bimal Dev TK</div>
        </div>
      </div> */}
    </div>
  );
}

export default Contact;
