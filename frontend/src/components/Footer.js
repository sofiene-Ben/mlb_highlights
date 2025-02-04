import React from "react";
import { Facebook, Twitter, Instagram } from "react-bootstrap-icons"; // Assurez-vous d'avoir installé bootstrap-icons

const Footer = () => {
  return (
    <footer className="bg-blue-900 text-white py-4 px-6">
      {/* Conteneur principal */}
      <div className="flex flex-col md:flex-row justify-between items-center gap-4">
        {/* Liens légaux */}
        <div className="text-center md:text-left text-sm legal">
          <a
            href="/mentions-legales"
            className="hover:text-gray-300 mr-4 inline-block"
          >
            Mentions légales
          </a>
          <a
            href="/terms-conditions"
            className="hover:text-gray-300 inline-block"
          >
            Termes & Conditions
          </a>
        </div>

        {/* Icônes réseaux sociaux */}
        <div className="flex justify-center space-x-6">
          <a
            href="https://www.facebook.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-gray-300"
          >
            <Facebook size={24} />
          </a>
          <a
            href="https://www.twitter.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-gray-300"
          >
            <Twitter size={24} />
          </a>
          <a
            href="https://www.instagram.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-gray-300"
          >
            <Instagram size={24} />
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
