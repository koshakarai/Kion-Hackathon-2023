import React from 'react';
import cards from './ps/some'
function Navigator() {
    return <div class="navbar">
        <div class="dropdown">
            <button class="dropbtn">
                File
                <i class="fa fa-caret-down"></i>
            </button>
            <div class="dropdown-content">
                <a id="open"> <input type="file" id="js-file" accept=".mp4" value="" onChange={(e) => cards(e)}/> </a>
                <a id="save">Save</a>
                <a href="#">New Scenes</a>
            </div>
        </div>
        <a href="#">Options</a>
        <a href="#overlay" class="tech">Tech</a>

    </div>
}

export default Navigator;