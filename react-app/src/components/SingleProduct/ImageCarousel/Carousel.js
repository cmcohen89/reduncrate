import React, { Children, useState, useEffect } from "react";
import classes from "./Carousel.module.css";

const widthSpan = 100;

export default function Carousel(props) {
  const [sliderPosition, setSliderPosition] = useState(0);
  const [touchStartPosition, setTouchStartPosition] = useState(0);
  const [touchEndPosition, setTouchEndPosition] = useState(0);
  const [touched, setTouched] = useState(false);
  const [swiped, setSwiped] = useState(false);
  const [mouseStartPosition, setMouseStartPosition] = useState(0);
  const [mouseEndPosition, setMouseEndPosition] = useState(0);
  const [mouseClicked, setMouseClicked] = useState(false);
  const [mouseSwiped, setMouseSwiped] = useState(false);

  const { children, infinite, imageLength } = props;

  // Slide Handlers
  const prevSlideHandler = () => {
    let newPosition = sliderPosition;

    if (newPosition > 0) {
      newPosition = newPosition - 1;
    } else if (infinite) {
      newPosition = imageLength - 1;
    }

    translateFullSlides(newPosition);
    setSliderPosition(newPosition);
  };

  const nextSlideHandler = () => {
    let newPosition = sliderPosition;
    if (newPosition < imageLength - 1) {
      newPosition = newPosition + 1;
    } else if (infinite) {
      newPosition = 0;
    }

    translateFullSlides(newPosition);
    setSliderPosition(newPosition);
  };

  const jumpToSlideHandler = (id) => {
    let toTranslate = id;
    translateFullSlides(toTranslate);
    setSliderPosition(id);
  };

  // Click Handlers
  const prevClickHandler = () => {
    prevSlideHandler();
  };

  const nextClickHandler = () => {
    nextSlideHandler();
  };

  // KeyPress Handler
  const keyPressHandler = (e) => {
    if (e.key === "ArrowLeft") {
      e.preventDefault();
      e.stopPropagation();
      prevSlideHandler();
      return;
    }

    if (e.key === "ArrowRight") {
      e.preventDefault();
      e.stopPropagation();
      nextSlideHandler();
      return;
    }
  };

  // Animation Speed
  const speedUpAnimation = () => {
    for (let i = 0; i < imageLength; i++) {
      let elem = document.getElementById(`carouselitem` + i);
      elem.classList.add(classes.FastAnimation);
    }
  };

  const slowDownAnimation = () => {
    for (let i = 0; i < imageLength; i++) {
      let elem = document.getElementById(`carouselitem` + i);
      elem.classList.remove(classes.FastAnimation);
    }
  };

  // Touch Handlers
  const touchStartHandler = (e) => {
    speedUpAnimation();
    setTouchStartPosition(e.targetTouches[0].clientX);
    setTouchEndPosition(e.targetTouches[0].clientX);
    setTouched(true);
  };

  const touchMoveHandler = (e) => {
    setTouchEndPosition(e.targetTouches[0].clientX);
    const frameWidth = document.getElementById("DisplayFrame").offsetWidth;
    const translateDist =
      ((touchEndPosition - touchStartPosition) / frameWidth) * 100;
    translatePartialSlides(translateDist);
    if (touched === true) {
      setSwiped(true);
    }
  };

  const touchEndHandler = (e) => {
    if (swiped) {
      slowDownAnimation();
      if (touchStartPosition - touchEndPosition > 75) {
        nextSlideHandler();
      } else if (touchStartPosition - touchEndPosition < -75) {
        prevSlideHandler();
      } else {
        jumpToSlideHandler(sliderPosition);
      }
    }
    setTouched(false);
    setSwiped(false);
  };

  // Mouse Handlers
  const mouseStartHandler = (e) => {
    e.preventDefault();
    speedUpAnimation();
    setMouseStartPosition(e.clientX);
    setMouseEndPosition(e.clientX);
    setMouseClicked(true);
  };

  const mouseMoveHandler = (e) => {
    e.preventDefault();
    var frameWidth = document.getElementById("DisplayFrame").offsetWidth;
    if (mouseClicked) {
      setMouseEndPosition(e.clientX);
      let translateDist =
        ((mouseEndPosition - mouseStartPosition) / frameWidth) * 100;
      translatePartialSlides(translateDist);
      setMouseSwiped(true);
    }
  };

  const mouseEndHandler = (e) => {
    slowDownAnimation();
    if (mouseSwiped === true) {
      if (mouseStartPosition - mouseEndPosition > 100) {
        nextSlideHandler();
      } else if (mouseStartPosition - mouseEndPosition < -100) {
        prevSlideHandler();
      } else {
        jumpToSlideHandler(sliderPosition);
      }
    }
    setMouseClicked(false);
    setMouseSwiped(false);
  };

  // Translate slides
  const translatePartialSlides = (toTranslate) => {
    let currentTranslation = -sliderPosition * widthSpan;
    let totalTranslation = currentTranslation + toTranslate;
    for (let i = 0; i < imageLength; i++) {
      let elem = document.getElementById(`carouselitem` + i);
      elem.style.transform = `translateX(` + totalTranslation + `%)`;
    }
  };

  const translateFullSlides = (newPosition) => {
    let toTranslate = -widthSpan * newPosition;
    for (var i = 0; i < imageLength; i++) {
      let elem = document.getElementById(`carouselitem` + i);
      elem.style.transform = `translateX(` + toTranslate + `%)`;
    }
  };

  const displayItems = Children.map(children, (child, index) => (
    <div className={classes.CarouselItem} id={`carouselitem` + index}>
      {child}
    </div>
  ));

  useEffect(() => {
    window.addEventListener("keydown", keyPressHandler);
    return () => {
      window.removeEventListener("keydown", keyPressHandler);
    };
  });

  return (
    <div>
      {imageLength > 1 ? (
        <div className={classes.ContainerCursor}>
          <div className={classes.LeftArrow} onClick={prevClickHandler}>
            <i className="fa-solid fa-chevron-left"></i>
          </div>
          <div
            onClick={nextClickHandler}
            id="DisplayFrame"
            className={classes.DisplayFrame}
            onTouchStart={(e) => touchStartHandler(e)}
            onTouchMove={(e) => touchMoveHandler(e)}
            onTouchEnd={(e) => touchEndHandler(e)}
            onMouseDown={(e) => mouseStartHandler(e)}
            onMouseMove={(e) => mouseMoveHandler(e)}
            onMouseUp={(e) => mouseEndHandler(e)}
            onMouseLeave={(e) => mouseEndHandler(e)}
          >
            {displayItems}
          </div>
          <div className={classes.RightArrow} onClick={nextClickHandler}>
            <i className="fa-solid fa-chevron-right"></i>
          </div>
        </div>
      ) : (
        <div className={classes.Container}>
          <div
            id="DisplayFrame"
            className={classes.DisplayFrame}
            onTouchStart={(e) => touchStartHandler(e)}
            onTouchMove={(e) => touchMoveHandler(e)}
            onTouchEnd={(e) => touchEndHandler(e)}
            onMouseDown={(e) => mouseStartHandler(e)}
            onMouseMove={(e) => mouseMoveHandler(e)}
            onMouseUp={(e) => mouseEndHandler(e)}
            onMouseLeave={(e) => mouseEndHandler(e)}
          >
            {displayItems}
          </div>
        </div>
      )}
    </div>
  );
}
