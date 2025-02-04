import React, { useState } from "react";

const Header = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <header>
            {/* Logo et titre */}

            <div className="navbar-color">
                <div className="logo-menu">
                    <h1 className="text-lg font-bold">
                        ✨ MLB - HighLight ✨
                    </h1>
                    {/* Bouton menu pour mobile */}
                    <nav className={`desktop-nav  `}>
                    <ul className="flex flex-col lg:flex-row gap-4">
                        <li>
                            <div>
                                <a href="/" className="hover:text-gray-300">
                                    Home
                                </a>
                            </div>
                        </li>
                        <li>
                            <a href="/preferences" className="hover:text-gray-300">
                                Preferences
                            </a>
                        </li>
                        <li>
                            <a href="/highlights" className="hover:text-gray-300">
                                Highlights
                            </a>
                        </li>
                        <li>
                            <a href="/login" className="hover:text-gray-300">
                                Login
                            </a>
                        </li>
                    </ul>
                </nav>
                    <button
                        className="text-white text-2xl lg:hidden"
                        onClick={toggleMenu}
                    >
                        {/* ☰ */}
                        {menuOpen ? (
                            <i className="bi bi-x-circle"></i> // Croix
                        ) : (
                            <i className="bi bi-list"></i> // Menu hamburger
                        )}
                    </button>
                </div>
            </div>


            {/* Menu navigation */}

            <div className={`navbar-color-2 ${menuOpen ? "active" : "hidden"}`}>
                <nav>
                    <ul className="flex flex-col lg:flex-row gap-4">
                        <li>
                            <div>
                                <a href="/" className="hover:text-gray-300">
                                    Home
                                </a>
                            </div>
                        </li>
                        <li>
                            <a href="/preferences" className="hover:text-gray-300">
                                Preferences
                            </a>
                        </li>
                        <li>
                            <a href="/highlights" className="hover:text-gray-300">
                                Highlights
                            </a>
                        </li>
                        <li>
                            <a href="/login" className="hover:text-gray-300">
                                Login
                            </a>
                        </li>
                    </ul>
                </nav>

            </div>
        </header>
    );
};

export default Header;


// import React, { useState } from "react";

// const Header = () => {
//     const [menuOpen, setMenuOpen] = useState(false);

//     const toggleMenu = () => {
//         setMenuOpen(!menuOpen);
//     };

//     return (
//         <header className="navbar-color">
//             <div className="container mx-auto px-4 flex justify-between items-center py-4">
//                 {/* Logo */}
//                 <h1 className="text-lg font-bold text-white">
//                     ✨ MLB - HighLight ✨
//                 </h1>

//                 {/* Navigation Desktop */}
//                 <nav className="hidden lg:flex space-x-6">
//                     <a href="/" className="hover:text-gray-300 text-white">
//                         Home
//                     </a>
//                     <a href="/preferences" className="hover:text-gray-300 text-white">
//                         Preferences
//                     </a>
//                     <a href="/highlights" className="hover:text-gray-300 text-white">
//                         Highlights
//                     </a>
//                     <a href="/login" className="hover:text-gray-300 text-white">
//                         Login
//                     </a>
//                 </nav>

//                 {/* Bouton Menu pour Mobile */}
//                 <button
//                     className="text-white text-2xl lg:hidden"
//                     onClick={toggleMenu}
//                 >
//                     {menuOpen ? (
//                         <i className="bi bi-x-circle"></i> // Croix
//                     ) : (
//                         <i className="bi bi-list"></i> // Menu hamburger
//                     )}
//                 </button>
//             </div>

//             {/* Menu Mobile */}
//             <div className={`navbar-color-2 ${menuOpen ? "block" : "hidden"} lg:hidden`}>
//                 <nav>
//                     <ul className="flex flex-col items-center gap-4 py-4">
//                         <li>
//                             <a href="/" className="hover:text-gray-300 text-white">
//                                 Home
//                             </a>
//                         </li>
//                         <li>
//                             <a href="/preferences" className="hover:text-gray-300 text-white">
//                                 Preferences
//                             </a>
//                         </li>
//                         <li>
//                             <a href="/highlights" className="hover:text-gray-300 text-white">
//                                 Highlights
//                             </a>
//                         </li>
//                         <li>
//                             <a href="/login" className="hover:text-gray-300 text-white">
//                                 Login
//                             </a>
//                         </li>
//                     </ul>
//                 </nav>
//             </div>
//         </header>
//     );
// };

// export default Header;
