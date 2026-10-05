// swift-tools-version: 5.9
// Package.swift — standalone Swift Package Manager CI fixture.
//
// Responsibilities
// - Declare the minimal library and XCTest targets used by hosted CI.
//
// Maintainer Notes
// - Keep the tools-version directive first; no signing or app targets.
import PackageDescription

let package = Package(
    name: "Fixture",
    products: [.library(name: "Fixture", targets: ["Fixture"])],
    targets: [
        .target(name: "Fixture"),
        .testTarget(name: "FixtureTests", dependencies: ["Fixture"])
    ]
)
